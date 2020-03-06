#Tyler Huang
#SoftDev1 pd2
#K11 -- Ay Mon Go Git It From Yer Flask
#2020-03-17

from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
import datetime
import json

app = Flask(__name__)
client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
col = client.d4.pokedex

@app.route("/")
def root():
    print(__name__)
    return render_template("landingpage.html")

@app.route("/type", methods=["POST"])
def getType():
	#print(request.form['types'])
	#print(get_type(request.form["types"])[0])
	#print(json.dumps(get_type(request.form["types"])))
	return render_template("returnpage.html", data=get_type(request.form["types"]))

def get_type(type):
	cursor = col.find({"type": type}, {"_id": 0, "name": 1, "img": 1, "type": 1})
	arr = []
	for document in cursor:
		arr.append(document)
	return arr

def get_rarity(spawn_Percentage):
    cursor = col.find({"spawn_chance": {"$lt": spawn_Percentage / 100} })
    for document in cursor:
        print(document)

if __name__ == "__main__":
    app.debug = True
    app.run()

