#Team Drumstick huangT wuJh
#Tyler Huang
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "fesgdfsdvf"

login = {'user': 'Bob', 'pass': '123'}
#session['login'] = 'admin'

@app.route("/")
def root():
    return render_template(
        "landingpage.html"
    )

@app.route("/auth", methods = ["POST"])
def authenticate():
    if (request.form['username'] != login['user'] and request.form['password'] == login['pass']):
        return redirect(url_for("errorPW"))
    if (request.form['username'] != login['user']):
        return redirect(url_for("errorUser"))
    if (request.form['password'] != login['pass']):
        return redirect(url_for("errorPass"))
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

@app.route("/errorPW")
def errorPW():
    return "Error: Username and Password Do Not Match. Go back and try again"

@app.route("/errorU")
def errorUser():
    return "Error: Username Does Not Match. Go back and try again"

@app.route("/errorP")
def errorPass():
    return "Error: Password Does Not Match. Go back and try again"

if __name__ == "__main__":
    app.debug = True
    app.run()
