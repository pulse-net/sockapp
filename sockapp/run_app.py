import argparse
import threading
import webbrowser
import os

from .app import app
from sockx.constants import *


def run_app():
    threading.Timer(0.5, lambda: webbrowser.open("http://localhost:5000")).start()

    parser = argparse.ArgumentParser(
        description="SockApp - Socket based file sharing app"
    )
    parser.add_argument("--port", default=PORT, help="Port in which socket will run")
    parser.add_argument(
        "--protocol", default=PROTOCOL, help="Protocol to use for sockets"
    )
    parser.add_argument(
        "--start_dir", default=os.getcwd(), help="Starting directory to send from or receive into"
    )
    parser.add_argument(
        "--debug", action="store_true", default=False, help="Start sockapp server in debug mode or not"
    )
    args = parser.parse_args()

    os.chdir(args.start_dir)

    app.config["port"] = args.port
    app.config["protocol"] = args.protocol
    app.run(debug=args.debug)
