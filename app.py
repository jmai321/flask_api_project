# app.py
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.utils import secure_filename
import os
from config import Config
from services.item_service import get_items, get_item, create_item, update_item, delete_item
from mock_db import USERS

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

# File upload configurations
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to validate allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify(message="Bad Request"), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify(message="Unauthorized"), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify(message="Not Found"), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify(message="Internal Server Error"), 500

# Authentication Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check user credentials against the mock database
    user = next((user for user in USERS if user["username"] == username and user["password"] == password), None)
    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

# Public Route
@app.route('/public', methods=['GET'])
def public():
    return jsonify(message="This is a public route accessible by anyone"), 200

# Protected Route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="You have accessed a protected route"), 200

# Admin Route
@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    return jsonify(message="Welcome to the admin route"), 200

# CRUD Routes for Items
@app.route('/items', methods=['GET'])
def list_items():
    return jsonify(get_items()), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    item = get_item(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify(message="Item not found"), 404

@app.route('/items', methods=['POST'])
@jwt_required()
def create_new_item():
    data = request.get_json()
    name = data.get("name")
    new_item = create_item(name)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_existing_item(item_id):
    data = request.get_json()
    name = data.get("name")
    updated_item = update_item(item_id, name)
    if updated_item:
        return jsonify(updated_item), 200
    else:
        return jsonify(message="Item not found"), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_existing_item(item_id):
    if delete_item(item_id):
        return jsonify(message="Item deleted"), 200
    else:
        return jsonify(message="Item not found"), 404

# File Upload Route
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify(message="No file part"), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(message="No selected file"), 400

    # Check if file type is allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify(message="File uploaded successfully"), 201
    else:
        return jsonify(message="File type not allowed"), 400

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
