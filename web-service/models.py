from utils import *
from db import *
from utils import encrypt_passw


def registr_new_user(email, passw):
    check_email(email)
    check_passw(passw)
    create_new_user_in_db(email, encrypt_passw(passw))
    return True

def to_auth(email, passw):
    check_email(email)
    check_passw(passw)
    return get_user_from_db(email, passw)
    
def get_requests(user_id):
    return get_requests_from_db(user_id)

def registr_new_personal_visit_request(request):
    return create_new_personal_visit_request(request)


