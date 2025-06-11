import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

from .mongo_class import Database

load_dotenv()

mongo = Blueprint("mongo", __name__)

@mongo.route("/api/mongo/createUser", methods=["POST"])
def createUser():
	request_data = request.get_json()
	userAuthID = request_data.get("thisUserID")

	print("userAuthID: ", userAuthID)

	database = Database()
	userInfo = database.getUserInformation(authID=userAuthID)

	if(userInfo):
		print("wow they existed before")
		return jsonify({"userMongoID": str(userInfo["_id"])}), 200

	print("wow they didn't exist before")
	newMongoID = database.createUser(
		"", 0, "", [], {},
		userAuthID, "", "", "", []
	)

	database.closeConnection()
	return jsonify({"userMongoID": str(newMongoID)}), 200

@mongo.route("/api/mongo/updateUserPerson", methods=["POST"])
def updateUserPerson():
	request_data = request.get_json()

	# print("request_data: ", request_data)

	userAuthID = request_data.get("authID")
	userDetails = request_data.get("newUserDetails")
	petDetails = request_data.get("newPetDetails")

	# print("authID: ", userAuthID)
	# print("userDetails: ", userDetails)
	# print("petDetails: ", petDetails)

	userName = None
	userAge = None
	userGender = None
	userLocation = None

	if(userDetails["name"] != "" and userDetails["name"] != None):
		userName = userDetails["name"]
	if(userDetails["age"] != '' and userDetails["age"] != None):
		userAge = userDetails["age"]
	if(userDetails["gender"] != "" and userDetails["gender"] != None):
		userGender = userDetails["gender"]
	if(userDetails["location"] != "" and userDetails["location"] != None):
		userLocation = userDetails["location"]

	petType = None
	petBreed = None
	petAge = None
	petGender = None
	petSize = None

	print("\n\nbreed: ", petDetails["breed"])

	if(petDetails["type"] != "" and petDetails["type"] != None):
		petType = petDetails["type"]
	if(petDetails["breed"] != "" and petDetails["breed"] != None):
		petBreed = petDetails["breed"]
	if(petDetails["age"] != "" and petDetails["age"] != None):
		petAge = petDetails["age"]
	if(petDetails["gender"] != "" and petDetails["gender"] != None):
		petGender = petDetails["gender"]
	if(petDetails["size"] != "" and petDetails["size"] != None):
		petSize = petDetails["size"]

	preferredAnimal = {
		"type": petType,
		"breed": petBreed,
		"age": petAge,
		"gender": petGender,
		"size": petSize
	}

	try:
		database = Database()
		userInfo = database.getUserInformation(authID=userAuthID)
		personID = userInfo["personTableID"]

		database.updateUserInformation(authID=userAuthID, location=userLocation)
		database.updatePersonInformation(personID=personID, name=userName, age=userAge, gender=userGender, preferred_animal=preferredAnimal)

		database.closeConnection()
		return jsonify({"success": "egg"}), 200
	
	except Exception as e:
		print("Error upddating user person: ", e)
		return jsonify({"error": e}), 500
	

@mongo.route("/api/mongo/getUserInfo", methods=["POST"])
def getUserInfo():
	request_data = request.get_json()
	userAuthID = request_data.get("authID")

	database = Database()
	userInfo = database.getUserInformation(authID=userAuthID)
	personInfo = database.getPersonInformation(personID=userInfo["personTableID"])

	userInfo["_id"] = str(userInfo["_id"])
	userInfo["personTableID"] = str(userInfo["personTableID"])
	personInfo["_id"] = str(personInfo["_id"])

	database.closeConnection()
	return jsonify({"userInfo": userInfo, "personInfo": personInfo}), 200
