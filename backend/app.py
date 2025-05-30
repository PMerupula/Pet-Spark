from flask import Flask, send_from_directory, request
from routes.pets_route import pets_blueprint
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(pets_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)