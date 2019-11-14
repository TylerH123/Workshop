#Tyler Huang
#SoftDev1 pd2
#K 25: Getting More REST
#2019-11-14

from flask import Flask, render_template
import urllib, json
app = Flask(__name__)

@app.route("/")
def route():
    u = urllib.request.urlopen('https://rickandmortyapi.com/api/character/')
    response = u.read()
    data = json.loads(response)
    img = data['results'][0]['image']
    img2 = data['results'][1]['image']
    u = urllib.request.urlopen('https://xkcd.com/614/info.0.json')
    response = u.read()
    data = json.loads(response)
    img3 = data['img']
    u = urllib.request.urlopen('https://www.balldontlie.io/api/v1/players')
    response = u.read()
    data = json.loads(response)
    name = data['data'][0]['first_name'] + ' ' + data['data'][0]['last_name']
    text = 'team name:' + data['data'][0]['team']['full_name']
    return render_template("index.html", pic = img, pic2 = img2, pic3 = img3, name = name, info = text)


if __name__ == "__main__":
    app.debug = True
    app.run()
