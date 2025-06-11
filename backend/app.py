# app.py

from flask import Flask
from flask_cors import CORS
from routes.auth import auth  # Adjust if your folder structure is different

app = Flask(__name__)

# Allow CORS from frontend (Svelte runs on port 5173)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Register Blueprint
app.register_blueprint(auth)

# Root test route (optional)
@app.route("/")
def index():
    return {"message": "Pet Spark API is running!"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)

# from flask import Flask, send_from_directory, request
# from routes.auth import auth_bp
# from dotenv import load_dotenv
# load_dotenv()

# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=True)

# app.register_blueprint(auth_bp, url_prefix='/api')