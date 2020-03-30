#Tyler Huang
#SoftDev1 pd2
#P03: TEDxSoftDev VII
#2020-03-27

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def root():
    print(__name__)
    return render_template("demo.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
