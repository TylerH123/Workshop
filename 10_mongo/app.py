#Tyler Huang, Jacob Olin, Hillary Zed
#SoftDev pd 2
#K10 -- Import/Export Bank
#2020-03-04

from pymongo import MongoClient
from pprint import pprint
import datetime
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client. 

def findByBorough(borough):
        for restaurant in restaurants.find({"borough": borough}):
                print(restaurant["name"])
