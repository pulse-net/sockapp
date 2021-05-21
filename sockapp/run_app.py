import argparse
import threading
import webbrowser

from .app import app
from .constants import *

def run_app():
    threading.Timer(0.5, lambda: webbrowser.open("http://localhost:5000")).start()

    parser = argparse.ArgumentParser(description="SockApp - Socket based file sharing app")
    parser.add_argument("--port", default=PORT, help="Port in which socket will run")
    parser.add_argument("--protocol", default=PROTOCOL, help="Protocol to use for sockets")
    args = parser.parse_args()

    app.config['port'] = args.port
    app.config['protocol'] = args.protocol
    app.run(debug=False)