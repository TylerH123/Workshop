#teamFakeMoonLanding_HuangT_BhuiyanS
#Tyler Huang
#SoftDev1 pd2
#K09: ’Tis Not a Race -- But You Will Go Faster
#2019-09-18

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def helloWorld():
    print(__name__)
    return "hello world"
    
@app.route("/my_foist_template")
def test_tmplt():
    coll = [0, 1, 2, 3, 4, 5]
    return render_template('my_foist_template.html', foo = "TeamFakeMoonLanding", collection = coll)
    print(__name__)

if __name__ == "__main__":
    app.debug = True
    app.run()
