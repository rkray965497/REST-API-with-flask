from flask import Flask, request, jsonify

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. In-memory data store for users (simple dictionary)
# Structure: {user_id: {"name": "...", "email": "..."}}
users = {}
current_id = 1 # Simple counter for new user IDs

# --- API Endpoints (Routes) ---

# A. GET all users or a specific user
@app.route('/users', methods=['GET'])
def get_users():
    """
    Handles GET requests.
    If a 'user_id' is provided in the query parameters, returns that user.
    Otherwise, returns all users.
    """
    user_id = request.args.get('user_id')

    if user_id:
        try:
            # Convert ID from string (query parameter) to integer
            uid = int(user_id)
            user = users.get(uid)
            if user:
                # Return the specific user data
                return jsonify({uid: user}), 200
            else:
                return jsonify({"error": f"User with ID {uid} not found"}), 404
        except ValueError:
            return jsonify({"error": "Invalid user_id format. Must be an integer."}), 400
    else:
        # Return all users
        return jsonify(users), 200

# B. POST (Create a new user)
@app.route('/users', methods=['POST'])
def create_user():
    """
    Handles POST requests to create a new user.
    Requires 'name' and 'email' in the JSON body.
    """
    global current_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email' field in request body"}), 400

    new_user = {
        "name": data['name'],
        "email": data['email']
    }

    # Store the new user and increment the ID counter
    users[current_id] = new_user
    new_user_id = current_id
    current_id += 1

    # Return the created user's data and a 201 Created status
    return jsonify({"message": "User created successfully", "id": new_user_id, "user": new_user}), 201

# C. PUT (Update an existing user)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Handles PUT requests to update an existing user by ID.
    The ID is part of the URL path.
    """
    data = request.get_json()

    if user_id not in users:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    # Update fields if they are provided in the request
    if 'name' in data:
        users[user_id]['name'] = data['name']
    if 'email' in data:
        users[user_id]['email'] = data['email']

    return jsonify({"message": "User updated successfully", "id": user_id, "user": users[user_id]}), 200

# D. DELETE (Remove a user)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Handles DELETE requests to remove a user by ID.
    The ID is part of the URL path.
    """
    if user_id not in users:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    # Remove the user from the dictionary
    del users[user_id]

    # Return a success message and a 204 No Content status (often used for successful DELETE)
    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    # Set debug=True for automatic reloading during development
    app.run(debug=True)
