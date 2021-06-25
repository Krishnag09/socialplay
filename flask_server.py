from flask import request
from flask import Flask, render_template
from flask_sock import Sock
import json
from mood_engine import mood_dict_engine
import selenium_aiva


app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def home():
    return render_template("index.html")

@sock.route('/communicate')
def websocketConn(ws):
  while True:
    sentJson = ws.receive()
    print(sentJson)
    sentData = json.loads(sentJson)
    print(sentData)
    moodSet = False
    for key, value in sentData.items():
      if key == 'emotion':
        mood = value
        genre = sentData['genre']
        moodSet = True
    
    if moodSet:
      key_signature = mood_dict_engine(mood)
      selenium_aiva.set_up()
      selenium_aiva.login()
      selenium_aiva.create_new_song(genre, key_signature)
      selenium_aiva.press_play()
      ws.send("music")
    else:
      ws.send("got it")



# Example: "localhost:5000/api/foo?a=hello&b=world"
# "localhost:5000/api/music?mood=happy&genre=electronic"
@app.route("/api/music", methods=['GET'])
def create_song():
    mood = request.args.get('mood')
    genre = request.args.get('genre')
    key_signature = mood_dict_engine(mood)

    selenium_aiva.create_new_song(genre, key_signature)
    try:
        selenium_aiva.press_play()
    except:
        selenium_aiva.press_play()

    return {"message": "success"}

# "localhost:5000/api/setup"
@app.route("/api/setup", methods=['GET'])
def setup():
    selenium_aiva.set_up()
    selenium_aiva.login()

    return {"message": "setting up"}


# "localhost:5000/api/play"
@app.route("/api/play")
def play():
    selenium_aiva.press_play()

    return "play"


# "localhost:5000/api/play"
@app.route("/api/refresh")
def ref():
    selenium_aiva.refresh()

    return "refresh"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) # or port=8080