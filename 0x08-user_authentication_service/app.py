#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort, make_response, \
    redirect, render_template
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """ basic route """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Add/Authenticate user """
    try:
        user = AUTH.register_user(request.form['email'],
                                  request.form['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ 11. Log in """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        sess = AUTH.create_session(email)
        form = {"email": email, "message": "logged in"}
        resp = make_response(jsonify(form))
        resp.set_cookie('session_id', sess)
        return resp
    else:
        abort(401)

    # data = request.form
    # if AUTH.valid_login(data['email'], data['password']):
    #     sess = AUTH.create_session(data['email'])
    #     resp = make_response({"email": data['email'],
    #                           "message": "logged in"})
    #     resp.set_cookie("session_id", sess)
    #     return resp
    # else:
    #     abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ 14. Log out """
    sess = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sess)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        return render_template(''), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
