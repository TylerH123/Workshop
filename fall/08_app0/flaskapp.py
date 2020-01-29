#Tyler Huang
#SoftDev1 pd2
#demo -- My First Flask App
#2019-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def route1():
    print(__name__)
    return "first route"

@app.route("/1")
def route2():
    print(__name__)
    print(__name__)
    return "second route"

@app.route("/2")
def route3():
    print(__name__)
    print(__name__)
    print(__name__)
    return "third route"

if __name__ == "__main__":
    app.debug = True
    app.run()
