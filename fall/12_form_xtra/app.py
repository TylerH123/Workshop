#Team Drumstick huangT abedinM
#Tyler Huang
#SoftDev1 pd2
#K12: Echo Echo Echo
#2019-09-27

from flask import Flask, render_template, request, session
import csv
app = Flask(__name__)

@app.route("/")
def helloWorld():
    print(__name__)
    return "hello world"

@app.route("/login")
def login():
    print(app)
    return render_template(
        "landingpage.html"
    )

@app.route("/authPost", methods = ["POST"])
def authenticatePost():
    print(app)
    print("--------------------")
    print(request)
    print("--------------------")
    print("method " + request.method)
    print("--------------------")
    print(request.form)
    print("--------------------")
    print("args: ")
    print(request.args)
    print("--------------------")
    print(request.form['username'])
    print("--------------------")
    print("cookies.get: ")
    print(request.cookies.get('username'))
    #print(request.headers)
    return render_template(
        "responsepage1.html",
        #user = request.cookies.get('username'),
        user = request.form['username'],
        method = request.method,
        greeting = "leave"
    )

@app.route("/authGet", methods = ["GET"])
def authenticateGet():
    print(app)
    print("--------------------")
    print(request)
    print("--------------------")
    print("method " + request.method)
    print("--------------------")
    print(request.form)
    print("--------------------")
    print("args: ")
    print(request.args)
    print("--------------------")
    print(request.args['username'])
    print("--------------------")
    #print(request.headers)
    return render_template(
        "responsepage2.html",
        #user = request.cookies.get('username'),
        user = request.form['username'],
        method = request.method,
        greeting = "leave"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
