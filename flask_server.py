from flask import Flask, render_template
from flask_sock import Sock
import json

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def home():
    return render_template("index.html")

@sock.route('/communicate')
def websocketConn(ws):
  while True:
    sentJson = ws.receive()
    sentData = json.loads(sentJson)
    print(sentData)
    ws.send("got it")