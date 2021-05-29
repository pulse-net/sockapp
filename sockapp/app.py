from flask import Flask, json, request, render_template, jsonify
import os
import socket

from . import __version__
from .utils.ip_helpers import get_ip
from .utils.file_dir_helpers import get_file_dir_path, untar_tarball
from .utils.path_helpers import parse_path
from sockx.constants import *
from sockx.receiver import Receiver
from sockx.sender import Sender
from sockx.utils.error import ConnectionFailure

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
            current_directory=os.getcwd(),
            version=__version__,
        )

@app.route("/messaging", methods=["GET"])
def messaging():

    if request.method == "GET":
        port = app.config.get("port", PORT)
        protocol = app.config.get("protocol", PROTOCOL)

        hostname = socket.gethostname()
        ip = get_ip()

        return render_template(
            "messaging.html",
            hostname=hostname,
            ip=ip,
            port=port,
            protocol=protocol,
            current_directory=os.getcwd(),
            version=__version__,
        )


@app.route("/send", methods=["POST"])
def send():

    if request.method == "POST":
        recv_ip = request.form["recv_ip"]
        send_path = request.form["send_path"]
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        sender_ip = get_ip()

        send_path = parse_path(path=send_path)

        if(sender_ip == recv_ip):
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": f"{sender_ip} is this system's IP, provide receiver's IP!",
                }
            )

        if not os.path.exists(send_path):
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": f"Path {send_path} not found!",
                }
            )

        file_path, is_dir = get_file_dir_path(path=send_path)
        sender = Sender.get_sender(
            filename=file_path, host=recv_ip, port=port, protocol=protocol
        )

        try:
            sender.send_file()
        except ConnectionFailure as e:
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": e.message,
                }
            )

        if is_dir:
            os.remove(file_path)        

        return jsonify(
            {"icon": "success", "title": "Success", "status": "File sent successfully!"}
        )

@app.route("/send-message", methods=["POST"])
def send_message():

    if request.method == "POST":
        recv_ip = request.form["recv_ip"]
        send_msg = request.form["send_msg"]
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        sender_ip = get_ip()

        if(sender_ip == recv_ip):
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": f"{sender_ip} is this system's IP, provide receiver's IP!",
                }
            )
            
        sender = Sender.get_sender(
            message=send_msg, host=recv_ip, port=port, protocol=protocol
        )
        
        try:
            sender.send_message()
        except ConnectionFailure as e:
            return jsonify(
                {
                    "icon": "error",
                    "title": "Error",
                    "status": e.message,
                }
            )

        return jsonify(
            {"icon": "success", "title": "Success", "status": "Message sent successfully!"}
        )

@app.route("/receive", methods=["POST"])
def receive():

    if request.method == "POST":
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        receiver = Receiver.get_receiver(port=port, protocol=protocol)
        filename = receiver.receive_file()

        if filename.endswith(".tar.gz"):
            untar_tarball(tarball_path=filename)

        return jsonify(
            {
                "icon": "success",
                "title": "Success",
                "status": "File received successfully!",
            }
        )

@app.route("/receive-message", methods=["POST"])
def receive_message():

    if request.method == "POST":
        port = int(app.config.get("port", PORT))
        protocol = app.config.get("protocol", PROTOCOL)

        receiver = Receiver.get_receiver(port=port, protocol=protocol, is_message=True)
        message = receiver.receive_message()

        return jsonify(
            {
                "icon": "success",
                "title": "Success",
                "status": "File received successfully!",
                "message": message
            }
        )

@app.route("/update-args", methods=["POST"])
def update_args():

    if request.method == "POST":
        port = request.form['port']
        protocol = request.form['protocol']
        cur_dir = request.form['cur_dir']

        app.config['port'] = port
        app.config['protocol'] = protocol
        os.chdir(cur_dir)

        return jsonify(
            {
                "icon": "success",
                "title": "Success",
                "status": "Information updated successfully!",
            }
        )