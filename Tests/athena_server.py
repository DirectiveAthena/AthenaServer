# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.models.version import Version

# Custom Packages
from AthenaServer.models.athena_server import AthenaServer
from AthenaServer.models.athena_server_methods import AthenaServerMethod
from AthenaServer.models.athena_server_command import AthenaServerCommand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestServer(AthenaServer):
    def __init__(self):
        super(TestServer, self).__init__(
            port=41768
        )
    # ------------------------------------------------------------------------------------------------------------------
    # - Define methods down below -
    # ------------------------------------------------------------------------------------------------------------------
    @AthenaServerMethod.Ping()
    def method_ping(self):
        print("pinged")

    @AthenaServerMethod.Command(AthenaServerCommand(name="alpha"))
    def method_command_alpha(self):
        print("ran command alpha")

    @AthenaServerMethod.Command(AthenaServerCommand(name="beta"))
    def method_command_beta(self):
        print("ran command beta")



# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    server = TestServer()
    server.start()

if __name__ == '__main__':
    main()