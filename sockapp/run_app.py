import argparse
import threading
import webbrowser

from .app import app

def run_app():
    threading.Timer(0.5, lambda: webbrowser.open("http://localhost:5000")).start()

    parser = argparse.ArgumentParser(description="SockApp - Socket based file sharing app")
    parser.add_argument("--port", default=5001, help="Port in which socket will run")
    args = parser.parse_args()

    app.config['port'] = args.port
    app.run(debug=False)