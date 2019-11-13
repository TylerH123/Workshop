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

if __name__ == "__main__":
    app.debug = True
    app.run()
