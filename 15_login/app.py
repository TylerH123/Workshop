#Team Drumstick huangT wuJh
#Tyler Huang
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, session, redirect, url_for
#from flask.ext.session import Session
app = Flask(__name__)

@app.route("/")
def root():
    return render_template(
        "landingpage.html"
    )

@app.route("/auth", methods = ["POST"])
def authenticate():
    if (request.form['username'] == '' and request.form['password'] == ''):
        return redirect(url_for("errorPW"))
    if (request.form['username'] == ''):
        return redirect(url_for("errorUser"))
    if (request.form['password'] == ''):
        return redirect(url_for("errorPass"))
    else:
        return render_template(
            "welcome.html",
            user = request.form['username'],
            password = request.form['password'],
            method = request.method,
            greeting = "hello"
        )

@app.route("/errorPW")
def errorPW():
    return "Error: No username and password found. Please enter a username and password"
@app.route("/errorU")
def errorUser():
    return "Error: No username found. Please enter a username"
@app.route("/errorP")
def errorPass():
    return "Error: No password found. Please enter a password"

if __name__ == "__main__":
    app.debug = True
    app.run()
