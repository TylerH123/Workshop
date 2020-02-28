#Tyler Huang and Joseph Y
#SoftDev pd 2
#K09 -- Yummy Mongo Py
#2020-02-28

from pymongo import MongoClient
from pprint import pprint
import datetime
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client.test
restaurants = db.restaurants 

def findByBorough(borough):
        for restaurant in restaurants.find({"borough": borough}):
                print(restaurant["name"])

def findByZipWithScoreCap(zip, score):
        for restaurant in restaurants.find({"address.zipcode" : str(zip), "grades.score": {"$lt": score}}):
                print(restaurant["name"])

def findByZip(zip): 
        for restaurant in restaurants.find({"address.zipcode" : str(zip)}):
                print(restaurant["name"])        

def findByZipAndGrade(zip, grade):
        for restaurant in restaurants.find({"address.zipcode" : str(zip), "grades.grade": grade}):
                print(restaurant["name"]) 

#findByZip(10282)
#findByZipAndGrade(10282, "A")