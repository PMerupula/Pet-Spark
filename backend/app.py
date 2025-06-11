from flask import Flask, send_from_directory, request
from routes.pets_route import pets_blueprint
from routes.auth import auth
from dotenv import load_dotenv
from flask_cors import CORS

from routes.mongo_route import mongo

load_dotenv()

app = Flask(__name__)

CORS(app, origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
])

app.register_blueprint(pets_blueprint, url_prefix='/api')
app.register_blueprint(auth)

app.register_blueprint(mongo)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)