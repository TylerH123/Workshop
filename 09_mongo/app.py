from pymongo import MongoClient
from pprint import pprint
import datetime
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client.test_db
restaurants = db.restaurants 



#with open("./primer-dataset.json", 'r') as file:
#    result = restaurants.insert_many(file)
        # pprint(data)

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
}

#restaurants.insert_one(post)

def findByZip(zip): 
        print(restaurants.find({"zip" : zip}))        
        #print(command) 


findByZip(1)     
#print(result)
# pprint(posts.find_one())