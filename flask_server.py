from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def home():
    return render_template("index.html")

@sock.route('/test')
def websocketConn(ws):
  while True:
    sentData = ws.receive()
    print(sentData)
    ws.send("got it")    