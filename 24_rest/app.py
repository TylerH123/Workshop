#Tyler Huang
#SoftDev1 pd2
#demo -- My First Flask App
#2019-09-18

from flask import Flask, render_template
import urllib, json
app = Flask(__name__)

@app.route("/")
def route():
    u = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=kg7tPvYHQboaf9UpESvapZ0YGie5sdPs6x59atjV')
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", explain = data['explanation'], pic = data['hdurl'])


if __name__ == "__main__":
    app.debug = True
    app.run()
