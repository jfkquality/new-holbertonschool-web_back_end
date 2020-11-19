#!/usr/bin/env python3

from flask import Flask, jsonify, request
from auth import Auth

Auth = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """ basic route """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Add/Authenticate user """
    try:
        user = Auth.register_user(request.form['email'],
                                  request.form['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
