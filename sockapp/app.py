from flask import Flask, request, render_template, jsonify

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
        return render_template("index.html")

@app.route("/send", methods=['POST'])
def send():

    if request.method == "POST":
        recv_ip = request.form['recv_ip']
        send_path = request.form['send_path']

        send_file(filename=send_path, host=recv_ip)

        return jsonify({"status": "File sent successfully!"})

@app.route("/receive", methods=['POST'])
def receive():

    if request.method == "POST":
        receive_file()

        return jsonify({"status": "File received successfully!"})