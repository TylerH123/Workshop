#Team Hotpot huangT wuJh
#Tyler Huang
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "fesgdfsdvf"

login = {'user': 'Bob', 'pass': '123'}
errMsg = ""
#session['login'] = 'admin'

@app.route("/")
def root():
    return render_template(
        "landingpage.html"
    )

@app.route("/auth", methods = ["POST"])
def authenticate():
    if (request.form['username'] != login['user'] or request.form['password'] != login['pass']):
        global errMsg
        errMsg = getErrorMsg()
        return redirect(url_for("error"))
    else:
        return render_template(
            "welcome.html",
            user = request.form['username'],
            password = request.form['password'],
            method = request.method,
            greeting = "hello"
        )

@app.route("/logout")
def logout():
    return render_template(
        "landingpage.html"
    )

@app.route("/error")
def error():
    print(errMsg)
    return render_template(
        "errorpage.html",
        errorMsg = errMsg
    )

@app.route("/return")
def returnPage():
    return redirect(url_for("root"))

def getErrorMsg():
    if (request.form['username'] != login['user'] and request.form['password'] != login['pass']):
        return "Incorrect username and password. Please go back and try again."
    if (request.form['username'] != login['user']):
        return "Incorrect username. Please go back and try again."
    if (request.form['password'] != login['pass']):
        return "Incorrect password. Please go back and try again."

if __name__ == "__main__":
    app.debug = True
    app.run()
