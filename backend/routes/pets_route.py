from flask import Blueprint, jsonify, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Creates a blueprint for pet-related routes
pets_blueprint = Blueprint('pets', __name__)

# Function to get the Petfinder API access token
def get_petAPI():
    url = "https://api.petfinder.com/v2/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("PETFINDER_API_KEY"),
        "client_secret": os.getenv("PETFINDER_SECRET")
    }
    # send a POST request to the Petfinder API to get the access token
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json().get("access_token")

# Route to get a list of pets with optional filters
@pets_blueprint.route('/pets', methods=['GET'])
def get_pets():
    token = get_petAPI()
    headers = {'Authorization': f'Bearer {token}'}

    # Build params dict with all possible filters
    params = {
        "page": request.args.get("page", 1),
        "limit": request.args.get("limit", 50),  # max is 100
        "sort": request.args.get("sort", "random"),
    }
    
    # Adds filters only if they have values
    if request.args.get("type"):
        params["type"] = request.args.get("type")
        
    if request.args.get("location"):
        params["location"] = request.args.get("location")
        
    if request.args.get("gender"):
        params["gender"] = request.args.get("gender")
        
    if request.args.get("age"):
        params["age"] = request.args.get("age")
        
    if request.args.get("breed"):
        params["breed"] = request.args.get("breed")

    # photos are returned here, it returns a small, medium, large and full photo in the response
    res = requests.get(
        "https://api.petfinder.com/v2/animals",
        headers=headers,
        params=params
    )
    
    return jsonify(res.json())

@pets_blueprint.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):
    token = get_petAPI()
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(
        f"https://api.petfinder.com/v2/animals/{pet_id}",
        headers=headers
    )
    return jsonify(res.json())

