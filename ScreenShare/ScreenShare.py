from ScreenShare import client
from ScreenShare import server


class ScreenShareClient:
    """
    This class will connect to people sharing their screen,
    and create a window to display the data it recieves.
    """

    def __init__(self, port):
        server.server(port)


class ScreenShare:
    """
    This class will share a device's screen with the specified host.
    """

    def __init__(self, host, port):
        client.client(host, port)
