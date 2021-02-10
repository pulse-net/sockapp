import webbrowser, threading

from .app import app

def run_app():
    threading.Timer(0.5, lambda: webbrowser.open("http://localhost:5000")).start()
    app.config['port'] = 1234
    app.run(debug=False)