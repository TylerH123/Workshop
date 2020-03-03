#Tyler Huang, Jacob Olin, Hillary Zed
#Team Sticky Sulphur
#SoftDev pd 2
#K10 -- Import/Export Bank
#2020-03-04

from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
col = client.stickySulphur.senators

def findByName(name):
	if " " not in name:
		pprint("full name required")
	else: 
		fname = name[:name.find(" ")]
		lname = name[name.find(" ")+1:]
		for senator in col.find({"person.firstname": fname, "person.lastname": lname}):
			pprint(senator)

def findByGender(gender: str):
	if gender is not "male" and gender is not "female": 
		pprint("please enter a valid gender")
	else: 
		for senator in col.find({"person.gender": gender}):
			pprint(senator)

#findByName("Lamar Alexander")
findByGender("male")