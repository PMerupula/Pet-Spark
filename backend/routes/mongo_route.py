import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

from .mongo_class import Database

load_dotenv()
# print("Environment variables loaded from .env file.")

mongo = Blueprint("mongo", __name__)

# AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")


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
	userAuthID = request_data.get("authID")
	userLocation = request_data.get("location")
	preferredAnimal = {
		"type": request_data.get("type"),
		"breed": request_data.get("breed"),
		"age": request_data.get("age"),
		"gender": request_data.get("gender"),
		"size": request_data.get("size")
	}

	try:
		database = Database()
		userInfo = database.getUserInformation(authID=userAuthID)
		personID = userInfo["personTableID"]

		database.updateUserInformation(authID=userAuthID, location=userLocation)
		database.updatePersonInformation(personID=personID, preferred_animal=preferredAnimal)

		database.closeConnection()
		return jsonify({"success": "egg"}), 200
	
	except Exception as e:
		print("Error upddating user person: ", e)
		return jsonify({"error": e}), 500
	
