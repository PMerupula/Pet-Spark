from pymongo import MongoClient
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
	def __init__(self):
		# mongoDB deployment's connection string.
		self.__uri = os.getenv("MONGO_DB_URI")
		self.__client = MongoClient(self.__uri)

	def ping(self):
		try:
			self.__client.admin.command('ping')
			print("Successfully pinged mongoDB database.")
		except Exception as e:
			print("Error pinging mongoDB database: ", e)

	# def getUserInformation():
	# 	# user table:
	# 	# 	id (auto-generated)
	# 	# 	authentication token (or whatever unique aspect authenticated accounts have)
	# 	# 	user's person table id
	# 	# 	location
	# 	# 	"people living with user" person table ids
	# 	# 	living situation (house, apartment, etc.)
	# 	# 	living situation notes (defined by user)
	# 	# 	current animals
	# 	# 		type (defined by Pet Finders API: Get Animal Types)
	# 	# 		breed (defined by Pet Finders API: Get Animal Breeds)
	# 	# 		size (small, medium, large, xlarge)
	# 	# 		gender (male, female, unknown/Not Applicable)
	# 	# 		age
	# 	# 		color (defined by Pet Finders API: Get Animal Types)
	# 	# 		coat (short, medium, long, wire, hairless, curly)
	# 	# 		name
	# 	# 		good_with_dogs
	# 	# 		good_with_cats
	# 	# 		health (not sure how we want to define this, but here are some example aspects)
	# 	# 			vaccination status
	# 	# 			general status (bad, good, great)

	# 	# insert data into database
	# 	collection = database.comets

	# 	# docs = [  # its in JSON format
	# 	# 	{     # will auto-generate an _id field value if not specified
	# 	# 		"name": "Comet 1",
	# 	# 		"officialName": "Singula Cometus"
	# 	# 	},
	# 	# 	{
	# 	# 		"name": "Comet 2",
	# 	# 		"officialName": "Duo Cometi"
	# 	# 	},
	# 	# 	{
	# 	# 		"name": "Comet 3",
	# 	# 		"officialName": "Tri Cometi"
	# 	# 	}
	# 	# ]
	# 	# result = collection.insert_many(docs)
	# 	# print(result)

	# def getPersonInformation():
		pass
		# person table:
		# 	id (auto-generated)
		# 	name
		# 	age
		# 	gender
		# 	allergens
		# 	preferred animal
		# 		type (defined by Pet Finders API: Get Animal Types)
		# 		breed (defined by Pet Finders API: Get Animal Breeds)
		# 		size (small, medium, large, xlarge)
		# 		gender (male, female, unknown/Not Applicable)
		# 		age
		# 		color (defined by Pet Finders API: Get Animal Types)
		# 		coat (short, medium, long, wire, hairless, curly)
		# 		name (user may want an animal with a pre-established name)
		# 		good_with_children
		# 		good_with_dogs
		# 		good_with_cats
		# 		house_trained
		# 		declawed
		# 		special_needs
		# 		vaccination status (saw this on the petdetails page, not sure how this is determined)


def main():
	print("starting")

	database = Database()
	database.ping()



	return

	# # MongoDB deployment's connection string.
	# uri = os.getenv("MONGO_DB_URI")

	# # client = MongoClient(uri, server_api=ServerApi('1'))
	# client = MongoClient(uri)

	# ping database
	# try:
	# 	client.admin.command('ping')
	# 	print("Successfully pinged mongoDB database.")
	# except Exception as e:
	# 	print("Error pinging mongoDB database: ", e)

	# getting data from database
	# database = client.sample_guides
	# collection = database.planets

	# retrieve data from database
	# results = collection.find()  # get all entries
	# results = collection.find({  # get entries with matching aspect
	# 	"hasRings": True
	# })
	# results = collection.find({  # get entries with multiple matching aspects
		# "hasRings": False,
		# "mainAtmosphere": "Ar"      # will search array for value
		# "surfaceTemperatureC.mean": # get entries whose attribute value
			# {"$lt": 15}             #    is less than 15
			# {"$gt": 15}             #    is greater than 15
		# "$and": [                   # another way of doing AND matches
		# 	{"orderFromSun": {"$gt": 2}},  # if this is done the other way
		# 	{"orderFromSun": {"$lt": 5}}   # the driver may only pick one
		# ]
		# "$or": [                      # OR matches
		# 	{"orderFromSun": {"$gt": 2}},
		# 	{"orderFromSun": {"$lt": 5}}
		# ]
	# })

	# iterate code
	# for doc in results:
	# 	print(doc)

	
	# insert data into database
	collection = database.comets

	# docs = [  # its in JSON format
	# 	{     # will auto-generate an _id field value if not specified
	# 		"name": "Comet 1",
	# 		"officialName": "Singula Cometus"
	# 	},
	# 	{
	# 		"name": "Comet 2",
	# 		"officialName": "Duo Cometi"
	# 	},
	# 	{
	# 		"name": "Comet 3",
	# 		"officialName": "Tri Cometi"
	# 	}
	# ]
	# result = collection.insert_many(docs)
	# print(result)


	# update data in database
	
	# doc = { 
	# 	"$mul": {"radius": 1.5}  # take existing value and multiply it by this value
	# }
	# result = collection.update_many({}, doc)  # update all entries with attribute
	# update operations result in an object with the amount of modified entries
	# print("Entries updated: ", result.modifed_count)

	
	# delete data from database
	# doc = {
	# 	"radius": {
	# 		"$gt": 2,
	# 		"$lt": 2
	# 	}
	# }
	# result = collection.delete_many(doc)  # deletes any entries matching criteria
	# deleting always results in an object with the number of entries deleted
	# print("Entries deleted: ", result.deleted_count)

	# close connection to database
	client.close()

if __name__ == "__main__":
	main()
