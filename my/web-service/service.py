from flask import Flask, jsonify, abort, request
from models import *
from exceptions import *


app = Flask(__name__)


@app.route("/registration", methods=['POST'])
def registr():
    req = request.json
    if (not req) or ('email' not in req) or ('password' not in req):
        abort(400)
    email = req['email']
    passw = req['password']

    try:
        registr_new_user(email, passw)
        return jsonify({'REGISTRATION_STATUS': 'successfully'}), 201
    except EmailNotValidError:
        return jsonify({'REGISTRATION_STATUS': 'failed', 'reason': 'Incorrect email!'}), 400
    except PasswordNotValidError:
        return jsonify({'REGISTRATION_STATUS': 'failed', 'reason': 'Incorrect password!'}), 400
    except UserAlreadyExistError:
        return jsonify({'REGISTRATION_STATUS': 'failed', 'reason': 'User already exist!'}), 400
    except ServerError:
        return jsonify({'REGISTRATION_STATUS': 'failed', 'reason': 'Server have some problems!'}), 404
    except ClientError:
        return jsonify({'REGISTRATION_STATUS': 'failed', 'reason': 'Client have some problems!'}), 404


@app.route("/login", methods=['POST'])
def login():
    req = request.json
    if (not req) or ('email' not in req) or ('password' not in req):
        abort(400)
    email = request.json['email']
    passw = request.json['password']

    try:
        token = to_auth(email, passw)
        return jsonify({'LOGIN': 'successfully', 'token': token}), 201
    except EmailOrPasswordIncorrectError:
        return jsonify({'LOGIN': 'failed', 'reason': 'Email or password is wrong!'}), 400
    except UserNotExistError:
        return jsonify({'LOGIN': 'failed', 'reason': "User doesn't exist !"}), 400
    except EmailNotValidError:
        return jsonify({'LOGIN': 'failed', 'reason': 'Incorrect email!'}), 400
    except PasswordNotValidError:
        return jsonify({'LOGIN': 'failed', 'reason': 'Password is unsafe!'}), 400
    except ServerError:
        return jsonify({'LOGIN': 'failed', 'reason': 'Server have some problems!'}), 404
    except ClientError:
        return jsonify({'LOGIN': 'failed', 'reason': 'Client have some problems!'}), 404


@app.route("/requests_list", methods=['POST'])
def get_requests_list():
    try:
        return jsonify({'REQUESTS_LIST': get_requests(request.json['user_id'])}), 201
    except ServerError:
        return jsonify({'REQUESTS_LIST': 'None', 'reason': 'Server have some problems!'}), 404
    except ClientError:
        return jsonify({'REQUESTS_LIST': 'None', 'reason': 'Client have some problems!'}), 404


@app.route("/registr_personal_request", methods=['POST'])
def send_request():
    try:
        registr_new_personal_visit_request(request.json)
        return jsonify({'REGISTRATION_REQUEST_STATUS': 'successfully'}), 201
    except ServerError:
        return jsonify({'REGISTRATION_REQUEST_STATUS': 'failed', 'reason': 'Server have some problems!'}), 404
    except ClientError:
        return jsonify({'REGISTRATION_REQUEST_STATUS': 'failed', 'reason': 'Client have some problems!'}), 404


if __name__ == "__main__":
    app.run()

