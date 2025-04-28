from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
import threading

class OSCListener:
    """
    Shared OSC listener to receive responses from AbletonOSC (e.g., selected track index).
    This class starts an OSC server on a fixed port and stores incoming values by address.
    """
    def __init__(self, ip="127.0.0.1", port=12000):
        self._ip = ip
        self._port = port
        self._dispatcher = Dispatcher()
        self._responses = {}

        self._server = ThreadingOSCUDPServer((self._ip, self._port), self._dispatcher)
        self._thread = threading.Thread(target=self._server.serve_forever)
        self._thread.daemon = True
        self._thread.start()

    def watch(self, address):
        """Start listening for responses to a specific OSC address."""
        def handler(addr, *args):
            if args:
                self._responses[addr] = args[0]
        self._dispatcher.map(address, handler)

    def get(self, address, timeout=1.0):
        """
        Wait for a value at a given OSC address.
        Should be called after AbletonOSC sends the corresponding /get/... request.
        """
        import time
        waited = 0
        interval = 0.05
        while waited < timeout:
            if address in self._responses:
                return self._responses.pop(address)
            time.sleep(interval)
            waited += interval
        return None
