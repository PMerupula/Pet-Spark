from pymongo import MongoClient
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
	def __init__(self):
		# mongoDB deployment's connection string.
		self.__uri = os.getenv("MONGO_DB_URI")
		self.__client = MongoClient(self.__uri)
		self.__establish()

	def __establish(self):
		print("Establishing reference to mongoDB databse...")
		try:
			self.__database = self.__client.pet_spark
			print("Successfully got reference to mongoDB database.")
		except Exception as e:
			print("Error getting reference: ", e)

	def ping(self):
		print("Pinging mongoDB...")
		try:
			self.__client.admin.command('ping')
			print("Successfully pinged mongoDB.")
		except Exception as e:
			print("Error pinging mongoDB: ", e)

	# person info object keys:
	# 	_id:  (string) unique ID in table
	# 	name:  (string)
	# 	age:  (int)
	# 	gender:  (string)
	# 	allergens:  (list of strings)
	# 	preferred_animal:  (object) person's preferred animal with the following keys
	# 		type:  (string) should match types found in Pet Finders API: Get Animal Types
	# 		breed:  (string) should match breeds found in Pet Finders API: Get Animal Breeds
	# 		size:  (string) small, medium, large, or xlarge
	# 		gender:  (string) male, female, or unknown/Not Applicable
	# 		age:  (int)
	# 		color:  (string) should match colors found in Pet Finders API: Get Animal Types)
	# 		coat:  (string) short, medium, long, wire, hairless, or curly
	# 		name:  (string)
	# 		good_with_children:  (boolean)
	# 		good_with_dogs:  (boolean)
	# 		good_with_cats:  (boolean)
	# 		house_trained:  (boolean)
	# 		declawed:  (boolean)
	# 		special_needs:  (boolean)
	# 		vaccination_status:  (string)
	def __createPerson(self, name:str, age:int, gender:str, allergens:list, preferred_animal:dict):
		print("Creating person entry...")
		# insert data into database
		collection = self.__database.persons

		docs = [{  # its in JSON format
			# will auto-generate an _id field value if not specified
			"name": name,
			"age": age,
			"gender": gender,
			"allergens": allergens,
			"preferred_animal": preferred_animal
		}]
		result = collection.insert_many(docs)
		
		print("Successfully created person entry.")
		return result.inserted_ids[0]

	def __removePerson(self, personToRemovePersonTableID:str):
		print("Removing person entry...")

		collection = self.__database.persons
		collection.delete_one({"_id": ObjectId(personToRemovePersonTableID)})

		print("Successfully removed person entry.")

	# user info object keys:
	# 	_id:  (string) unique ID in table
	# 	authID:  (string) user authentication token from logging in
	# 	personTableID:  (string) user's ID in the person table
	# 	location:  (string)  location
	# 	associatedPersons:  (array of strings) person table ids
	# 	livingSituation:  (string) living situation type
	# 	livingSituationNotes:  (string) living situation notes defined by user
	# 	currentAnimals:  (array of objects) animal objects with the following keys
	# 		type:  (string) should match types found in Pet Finders API: Get Animal Types
	# 		breed:  (string) should match breeds found in Pet Finders API: Get Animal Breeds
	# 		size:  (string) small, medium, large, or xlarge
	# 		gender:  (string) male, female, or unknown/Not Applicable
	# 		age:  (int)
	# 		color:  (string) should match colors found in Pet Finders API: Get Animal Types)
	# 		coat:  (string) short, medium, long, wire, hairless, or curly
	# 		name:  (string)
	# 		good_with_dogs:  (boolean)
	# 		good_with_cats:  (boolean)
	# 		health:  (object with the following keys)
	# 			vaccination_status:  (string)
	# 			status:  (string) bad, good, great, other ones that we may want to add
	def createUser(self,
		name:str, age:int, gender:str, allergens:list, preferred_animal:dict,
		authID, location, livingSituation:str, livingSituationNotes:str, currentAnimals:list
	):
		print("Creating user entry...")	
		personTableID = self.__createPerson(name, age, gender, allergens, preferred_animal)
		collection = self.__database.users

		docs = [{  # its in JSON format
			# will auto-generate an _id field value if not specified
			"authID": authID,
			"personTableID": personTableID,
			"location": location,
			"associatedPersons": [],
			"livingSituation": livingSituation,
			"livingSituationNotes": livingSituationNotes,
			"currentAnimals": currentAnimals
		}]
		result = collection.insert_many(docs)
		
		print("Successfully created user entry.")
		return result.inserted_ids[0]
	
	def addPersonToUser(self, userID:str,
		name:str, age:int, gender:str, allergens:list, preferred_animal:dict
	):
		print("Addding person to user's associated persons...")
		personID = self.__createPerson(name, age, gender, allergens, preferred_animal)

		collection = self.__database.users
		collection.update_one({"_id": ObjectId(userID)}, {"$push": {"associatedPersons": personID}})

		print("Successfully added person to user's associated persons.")
		return personID
	
	def removePersonFromUser(self, userID:str, personToRemovePersonTableID:str):
		print("Removing person from user's associated persons...")
		collection = self.__database.users
		collection.update_one({"_id": ObjectId(userID)}, {"$pull": {"associatedPersons": ObjectId(personToRemovePersonTableID)}})
		
		self.__removePerson(personToRemovePersonTableID)

		print("Successfully removed person from user's associated persons.")

def main():
	print("Starting")

	# print(ObjectId("6847986a9d7f80c5de6ce678"))
	# return

	myDatabase = Database()
	myDatabase.ping()

	# create user example
	# userPersonTableID = myDatabase.createUser(
	# 	"myName", 1, "testGender", ["testAllergy1", "testAllergy2"], {
	# 		"type": "testType",
	# 		"breed": "testBreed",
	# 		"size": "testSize",
	# 		"gender": "testGender",
	# 		"age": 1,
	# 		"color": "testColor",
	# 		"coat": "testCoat",	
	# 		"name": "testName",
	# 		"good_with_children": True,
	# 		"good_with_dogs": True,
	# 		"good_with_cats": True,
	# 		"house_trained": True,
	# 		"declawed": True,
	# 		"special_needs": True,
	# 		"vaccination_status": "yes"
	# 	},
	# 	"testAuthID", "testLocation", "testLivingSituation", "testLivingSituationNotes", [
	# 		{
	# 			"type": "testType",
	# 			"breed": "testBreed",
	# 			"size": "testSize",
	# 			"gender": "testGender",
	# 			"age": 1,
	# 			"color": "testColor",
	# 			"coat": "testCoat",	
	# 			"name": "testName1",
	# 			"good_with_dogs": True,
	# 			"good_with_cats": True,
	# 			"health": {
	# 				"vaccination_status": "yes",
	# 				"status": "testStatus"
	# 			}
	# 		},
	# 		{
	# 			"type": "testType",
	# 			"breed": "testBreed",
	# 			"size": "testSize",
	# 			"gender": "testGender",
	# 			"age": 1,
	# 			"color": "testColor",
	# 			"coat": "testCoat",	
	# 			"name": "testName2",
	# 			"good_with_dogs": True,
	# 			"good_with_cats": True,
	# 			"health": {
	# 				"vaccination_status": "yes",
	# 				"status": "testStatus"
	# 			}
	# 		}
	# 	]
	# )
	# print(userPersonTableID)

	# add associated person to user
	# addedPersonPersonTableID = myDatabase.addPersonToUser("6847aef2c81abe261e2026e9",
	# 	"testAssociate", 1, "testGender", ["testAllergy1", "testAllergy2"], {
	# 		"type": "testType",
	# 		"breed": "testBreed",
	# 		"size": "testSize",
	# 		"gender": "testGender",
	# 		"age": 1,
	# 		"color": "testColor",
	# 		"coat": "testCoat",	
	# 		"name": "testNameA",
	# 		"good_with_children": True,
	# 		"good_with_dogs": True,
	# 		"good_with_cats": True,
	# 		"house_trained": True,
	# 		"declawed": True,
	# 		"special_needs": True,
	# 		"vaccination_status": "yes"
	# 	}
	# )
	# print(addedPersonPersonTableID)

	# remove associated person from user
	# myDatabase.removePersonFromUser("6847aef2c81abe261e2026e9", "6847b15abc34d2315545b732")

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
