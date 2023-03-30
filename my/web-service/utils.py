from exceptions import EmailNotValidError, PasswordNotValidError

import re
import string, secrets
from crypt import crypt, METHOD_MD5


# for email validate
regex_email = re.compile('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}')
# for password validate 
regex_passw = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&^])[A-Za-z\d@$!#%*?&^]{8,20}$')


def generate_new_user_token(size=42):
    letters = string.ascii_lowercase+string.ascii_uppercase+string.digits            
    return ''.join(secrets.choice(letters) for i in range(size))

def encrypt_passw(passw):
    return crypt(passw, '$1$LhYMX2Do$glkG7XdgA8QedvxtN5Uv6.')

def check_passw(passw: str):
    if(re.fullmatch(regex_passw, passw)):
        return True
    else:
        print(re.fullmatch(regex_passw, passw))
        raise PasswordNotValidError('Invalid password')

def check_email(email: str):
    if(re.fullmatch(regex_email, email)):
        return True
    else:
        raise EmailNotValidError('Invalid Email')


# check_email('cry.warface@yandex.ru')
# check_passw('123snNs&*Qfst')
# print(generate_new_user_token(42))
# print(encrypt_passw('1asfalsdfj'))

