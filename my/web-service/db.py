import requests as req
from utils import generate_new_user_token, encrypt_passw
from exceptions import (
        UserNotExistError, 
        EmailOrPasswordIncorrectError, 
        ServerError,
        ClientError
        )

from config import API_SERVER_ADDRESS


def create_new_user_in_db(email, passw):
    post_data = {
            'email':email,
            'password':passw
            }
    response = req.post(
            API_SERVER_ADDRESS+"/users",
            json=post_data
            )
    if str(response.status_code)[0] == '5':
        raise ServerError(f"Response code: {response.status_code}")
    if str(response.status_code)[0] == '4':
        raise ClientError(f"Response code: {response.status_code}")
    print('registration', response.status_code)
    return True

def get_user_from_db(email, passw):
    response = req.get(
            API_SERVER_ADDRESS+f"/users/{email}",
            )

    if str(response.status_code)[0] == '5':
        raise ServerError(f"Response code: {response.status_code}")
    if str(response.status_code)[0] == '4':
        raise ClientError(f"Response code: {response.status_code}")
    
    if response.json()['password'] != encrypt_passw(passw):
        raise EmailOrPasswordIncorrectError
    print('login ', response.status_code)
    return generate_new_user_token()

def get_requests_from_db(user_id):
    response = req.get(
            API_SERVER_ADDRESS+f"/requests/list/{user_id}",
            )
    if str(response.status_code)[0] == '5':
        raise ServerError(f"Response code: {response.status_code}")
    if str(response.status_code)[0] == '4':
        raise ClientError(f"Response code: {response.status_code}")
    print('get_request_list', response.status_code)
    return response.json()

def create_new_personal_visit_request(request: dict):
    response = req.post(
            API_SERVER_ADDRESS+"/requests",
            json=request
            )
    if str(response.status_code)[0] == '5':
        raise ServerError(f"Response code: {response.status_code}")
    if str(response.status_code)[0] == '4':
        raise ClientError(f"Response code: {response.status_code}")

    print('create_new_personal_visit_request', response.status_code)
    return True

def verificate_token():
    pass


