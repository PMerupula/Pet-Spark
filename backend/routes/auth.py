import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()
# print("Environment variables loaded from .env file.")

auth = Blueprint("auth", __name__)

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")

AUTH0_M2M_CLIENT_ID = os.getenv("AUTH0_M2M_CLIENT_ID")
AUTH0_M2M_CLIENT_SECRET = os.getenv("AUTH0_M2M_CLIENT_SECRET")

AUTH0_RWA_CLIENT_ID = os.getenv("AUTH0_RWA_CLIENT_ID")
AUTH0_RWA_CLIENT_SECRET = os.getenv("AUTH0_RWA_CLIENT_SECRET")


def get_access_token():
    """
    Fetches one access token from Auth0 that will be used for all of the API calls.
    """
    access_token_endpoint = f"https://{AUTH0_DOMAIN}/oauth/token"
    payload = {
        "client_id": AUTH0_M2M_CLIENT_ID,
        "client_secret": AUTH0_M2M_CLIENT_SECRET,
        "audience": AUTH0_AUDIENCE,
        "grant_type": "client_credentials"
    }

    response = requests.post(access_token_endpoint, json=payload)
    if(response.status_code != 200):
       # print("Couldn't get the access token from Auth0: ", response.text)
        raise Exception("Failed to retrieve the access token.")
   # print("Response: ", response.json())
    access_token = response.json().get("access_token")
   # print("Access token: ", access_token)
    return access_token

@auth.route("/api/authentication/register", methods=["POST"])
def register():
    """
    Registers a new user in Auth0 using the built-in Auth0 Management API.
    Required input: JSON request containing the user's email and password.
    """
    request_data = request.get_json()
    user_email = request_data.get("email")
    user_password = request_data.get("password")
    
   # print(f"Registering user with email: {user_email}")
    
    if(not user_email or not user_password):
       # print("Email and password are required for registration. Missing either email or password.")
        return jsonify({"error": "Email and password are required"}), 400
    try:
        access_token = get_access_token()
       # print("Access token retrieved successfully.")
       # print(f"Access token: {access_token[:10]}...")
    except Exception as e:
       # print("Error retrieving access token:", str(e))
        return jsonify({"error": "Failed to retrieve access token"}), 500
    
    register_endpoint = f"https://{AUTH0_DOMAIN}/api/v2/users"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "email": user_email,
        "password": user_password,
        "connection": "Username-Password-Authentication"
    }
    response = requests.post(
        register_endpoint,
        headers=headers,
        json=payload
    )
   # print("Sent request to:", register_endpoint)
   # print("Request headers:", headers)
   # print("Request payload:", payload)
   # print("Response status code:", response.status_code)
   # print("Response text:", response.text)

    if response.status_code != 201:
       # print("Failed to create user:", response.text)
        return jsonify({"error": "Failed to create user"}), response.status_code

    user_id = response.json().get("user_id")
    #print(f"User created successfully with ID: {created_user_id}")
    return jsonify({"message": "User created successfully", "user_id": user_id}), 201

@auth.route("/api/authentication/login", methods=["POST"])
def login():
    """
    Logs the user in via the built-in Auth0 Management API.
    Required input: JSON request containing the user's email and password.
    Returns an access token if successful.
    """
    request_data = request.get_json()
    user_email = request_data.get("email")
    user_password = request_data.get("password")
    
    #print("Logging in")

    if(not user_email or not user_password):
       # print("Email and password are required for login. Missing either email or password.")
        return jsonify({"error": "Email and password are required"}), 400

    login_endpoint = f"https://{AUTH0_DOMAIN}/oauth/token"

    payload = {
        "grant_type": "password",
        "username": user_email,
        "password": user_password,
        "audience": AUTH0_AUDIENCE,
        "client_id": AUTH0_RWA_CLIENT_ID,
        "client_secret": AUTH0_RWA_CLIENT_SECRET,
        "scope": "openid profile email"
    }

    response = requests.post(login_endpoint, json=payload)
    if(response.status_code != 200):
       # print("Failed to log in:", response.text)
        return jsonify({"error": "Failed to log in"}), response.status_code
    
    access_token = response.json().get("access_token")
    user_info_endpoint = f"https://{AUTH0_DOMAIN}/userinfo"
    user_info_response = requests.get(user_info_endpoint, headers={
        "Authorization": f"Bearer {access_token}"  
    })
    if user_info_response.status_code != 200:
        #print("Failed to retrieve user information:", user_info_response.text)
        return jsonify({"error": "Failed to retrieve user information"}), user_info_response.status_code
    user_info = user_info_response.json()
    user_id = user_info.get("sub")
    return jsonify({"user_id": user_id}), 200