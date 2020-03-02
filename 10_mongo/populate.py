from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client.teamName
col = db.senators

with open("./role.json", 'r') as file:
    data = json.load(file)
    #print(data['objects'][0])
    for member in data['objects']:
        id = col.insert_one(loads(json.dumps(member)))
        print(id)

