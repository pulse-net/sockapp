from flask import Flask, json, request, render_template, jsonify
import os
import socket

from . import __version__
from .ip_helpers import get_ip
from .constants import *
from .receiver.receiver import Receiver
from .sender.sender import Sender

# Instantiate flask app
app = Flask(__name__)

# Basic config for flask app
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "my-secret-key"
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["GET"])
def index():

    if request.method == "GET":
        port = app.config.get("port", PORT)
        protocol = app.config.get("protocol", PROTOCOL)

        hostname = socket.gethostname()
        ip = get_ip()

        return render_template(
            "index.html",
            hostname=hostname,
            ip=ip,
            port=port,
            protocol=protocol,
            version=__version__,
        )


@app.route("/send", methods=["POST"])
def send():

    if request.method == "POST":
        recv_ip = request.form["recv_ip"]
        send_path = request.form["send_path"]
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        if not os.path.exists(send_path):
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": f"Path {send_path} not found!",
                }
            )

        sender = Sender.get_sender(
            filename=send_path, host=recv_ip, port=port, protocol=protocol
        )
        sender.send_file()

        return jsonify(
            {"icon": "success", "title": "Success", "status": "File sent successfully!"}
        )


@app.route("/receive", methods=["POST"])
def receive():

    if request.method == "POST":
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        receiver = Receiver.get_receiver(port=port, protocol=protocol)
        receiver.receive_file()

        return jsonify(
            {
                "icon": "success",
                "title": "Success",
                "status": "File received successfully!",
            }
        )
