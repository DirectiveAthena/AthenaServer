# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from typing import Callable
from dataclasses import dataclass, field

# Custom Library
from AthenaLib.models.time import TimeValue, Minute

# Custom Packages
from AthenaServer.models.handlers.handler_data import HandlerData
from AthenaServer.models.outputs.output import Output
from AthenaServer.models.responses.response import Response
from AthenaServer.models.responses.response_server import Response_AthenaServer
from AthenaServer.data.return_codes import ErrorClient

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class AthenaServerProtocol(asyncio.Protocol):
    output_types:list[type[Output]]
    handler_data:HandlerData

    # non init
    tasks:set=field(init=False, default_factory=set)
    closed:bool=field(init=False, default=False)
    transport: asyncio.transports.Transport = field(init=False, repr=False)
    loop:asyncio.AbstractEventLoop=field(init=False, repr=False)
    outputs:list[Output] = field(init=False, repr=False, default_factory=list)

    def __post_init__(self):
        self.loop = asyncio.new_event_loop()

    # ------------------------------------------------------------------------------------------------------------------
    # - factory, needed for asyncio.AbstractEventLoop.create_connection protocol_factory kwarg used in Launcher -
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    def factory(cls, **kwargs) -> Callable[[], AthenaServerProtocol]:
        """
        Factory is used by 'asyncio.AbstractEventLoop.create_connection' to return a callable object.
        This way extra kwargs can be passed to the protocol without the need for a lambda
        """
        def factory_wrapper():
            # noinspection PyArgumentList
            return cls(**kwargs)
        return factory_wrapper

    # ------------------------------------------------------------------------------------------------------------------
    # - asyncio.Protocol methods -
    # ------------------------------------------------------------------------------------------------------------------
    def connection_made(self, transport: asyncio.transports.Transport) -> None:
        """
        Gets run when a client connects to the server
        Stores the 'asyncio.transports.Transport' as a attr of the class
        """
        self.transport = transport
        self.outputs = [o(transport=transport) for o in self.output_types]
        task = asyncio.create_task(self.task_ping())
        self.tasks.add(task)

    def data_received(self, data: bytearray) -> None:
        """
        Gets run when a client sends data to server
        """
        asyncio.create_task(self.task_data_received(data))

    async def task_data_received(self, data:bytearray):
        for output in self.outputs:
            await output.on_receive(data)

        # only generate one response, and output it accordingly
        response: Response = await self.handler_data.handle(data)

        for output in self.outputs:
            await output.send(response)

        if isinstance(response, Response_AthenaServer) and response.code == ErrorClient.RequestTimeout:
            self.transport.close()

    def connection_lost(self, exc: Exception | None) -> None:
        """
        Gets run when a client looses connection to the server
        """
        if exc is not None:
            print(exc)
        self.transport.close()
        self.closed = True

    # ------------------------------------------------------------------------------------------------------------------
    # - Ping Task -
    # ------------------------------------------------------------------------------------------------------------------
    # todo don't make this hardcoded
    async def task_ping(self, interval:TimeValue=Minute(1)):
        interval_sec = interval.to_int_as_seconds()
        while not self.closed:
            await asyncio.sleep(interval_sec)
            for output in self.outputs:
                await output.send_ping()
