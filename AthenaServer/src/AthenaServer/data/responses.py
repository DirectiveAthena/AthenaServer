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
INTERNAL_ERROR = Response_AthenaServer(code=ErrorServer.InternalError)
INTERNAL_ERROR_ENCODED:bytes = INTERNAL_ERROR.encode()

NOT_FOUND = Response_AthenaServer(code=ErrorClient.NotFound)
BAD_REQUEST = Response_AthenaServer(code=ErrorClient.BadRequest)
NOT_ACCEPTABLE = Response_AthenaServer(code=ErrorClient.NotAcceptable)

PING = Response_AthenaServer(code=Information.Ping,body={"AthenaServer":"Send me back"})
PING_ENCODED:bytes = PING.encode()