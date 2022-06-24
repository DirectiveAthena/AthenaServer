# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from typing import Callable
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_data_handler import AthenaServerDataHandler
from AthenaServer.models.athena_server_methods import MethodPing
import AthenaServer.models.exceptions as exceptions
from AthenaServer.models.outputs.output import Output

import AthenaServer.functions.output_callbacks as output_callbacks

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class AthenaServerProtocol(asyncio.Protocol):
    output_types:list[type[Output]] = None
    data_handler:AthenaServerDataHandler=None
    ping_callback:MethodPing=None

    # non init
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
        """
        # noinspection PyArgumentList
        self.outputs = [o(transport=transport) for o in self.output_types]

        self.transport = transport
        self.ping_callback.callback()

    def data_received(self, data: bytearray) -> None:
        """
        Gets run when a client sends data to server
        """
        try:
            self.data_handler.handle(data)

        except exceptions.JsonNotFound:
            self.output_handler(output_callbacks.json_not_found)
        except exceptions.WrongFormat:
            self.output_handler(output_callbacks.wrong_format)


    def connection_lost(self, exc: Exception | None) -> None:
        """
        Gets run when a client looses connection to the server
        """
        print(exc)

    def eof_received(self) -> bool | None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # - Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def output_handler(self,callback:Callable):
        for output in self.outputs:
            callback(output)