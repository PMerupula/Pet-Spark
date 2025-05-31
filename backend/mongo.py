from pymongo import MongoClient
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

def main():
	print("starting")

	# MongoDB deployment's connection string.
	uri = os.getenv("MONGO_DB_URI")

	# client = MongoClient(uri, server_api=ServerApi('1'))
	client = MongoClient(uri)

	# Send a ping to confirm a successful connection
	try:
		client.admin.command('ping')
		print("Pinged your deployment. You successfully connected to MongoDB!")
	except Exception as e:
		print(e)

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

	# Close the connection to MongoDB when you're done.
	client.close()

if __name__ == "__main__":
	main()
