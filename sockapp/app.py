from flask import Flask, json, request, render_template, jsonify
import os
import socket

from .sender import send_file
from .receiver import receive_file

# Instantiate flask app
app = Flask(__name__)

# Basic config for flask app
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "my-secret-key"
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=['GET'])
def index():

    if request.method == "GET":
        port = app.config.get('port', 5001)

        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        return render_template("index.html", hostname=hostname, ip=ip, port=port)

@app.route("/send", methods=['POST'])
def send():

    if request.method == "POST":
        recv_ip = request.form['recv_ip']
        send_path = request.form['send_path']

        if not os.path.exists(send_path):
            return jsonify({"icon": "error", "title": "Error", "text": f"Path {send_path} not found!"})

        send_file(filename=send_path, host=recv_ip)

        return jsonify({"icon": "success", "title": "Success", "status": "File sent successfully!"})

@app.route("/receive", methods=['POST'])
def receive():

    if request.method == "POST":
        receive_file()

        return jsonify({"icon": "success", "title": "Success", "status": "File received successfully!"})