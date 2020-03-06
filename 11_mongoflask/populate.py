from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client.d4
col = db.pokedex

with open("./pokedex.json", 'r') as file:
    data = json.load(file)
    #print(data['objects'][0])
    for member in data['pokemon']:
        col.insert_one(loads(json.dumps(member)))
        #print(member)

