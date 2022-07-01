# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServerClient.models.non_linear.handlers.handler_data import HandlerData
from AthenaServerClient.models.REST_request import RESTRequest
from AthenaServerClient.data.rest import Commands

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class HandlerData_Client(HandlerData):

    async def handle(self, data: bytearray) -> RESTRequest|None:
        match (data_dict := json.loads(data)):
            # ping command
            case {"code":105, "body": {"AthenaServer": str(response)}}:
                request =  RESTRequest(
                    rest_command=Commands.POST,
                    orm=f"{self.root_name}/ping",
                    body={"response":response}
                )
                print(request)
                return request
        print(data_dict)
        return data_dict


