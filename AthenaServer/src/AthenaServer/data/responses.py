# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json

# Custom Library

# Custom Packages
from AthenaServer.models.responses.response_server import Response_AthenaServer
from AthenaServer.data.return_codes import *
from AthenaServer.data.general import UTF_8

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
INTERNAL_ERROR = Response_AthenaServer(code=ErrorServer.InternalError,body={})
INTERNAL_ERROR_ENCODED:bytes = f"{json.dumps(INTERNAL_ERROR.to_dict())}\r\n".encode(UTF_8)

NOT_FOUND = Response_AthenaServer(code=ErrorClient.NotFound, body={})
BAD_REQUEST = Response_AthenaServer(code=ErrorClient.BadRequest, body={})
NOT_ACCEPTABLE = Response_AthenaServer(code=ErrorClient.NotAcceptable, body={})