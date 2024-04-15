#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user database (replace with secure storage)
users = {
    "admin": "password123",
    "user1": "securepass"
}

def authenticate(username, password):
    return username in users and users[username] == password

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if authenticate(username, password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    else:
        return jsonify({"message": "Username and password required"}), 400

if __name__ == '__main__':
    app.run(debug=True)

