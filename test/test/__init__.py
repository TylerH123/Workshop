#Tyler Huang
#SoftDev1 pd2
#demo -- My First Flask App
#2019-09-18

from flask import Flask, render_template
import os
app = Flask(__name__)

DIR = os.path.dirname(__file__) or '.'
DIR += '/'

@app.route("/")
def route1():
    print(__name__)
    return "first route"

if __name__ == "__main__":
    app.debug = True
    app.run()