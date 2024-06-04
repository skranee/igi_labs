from django.contrib.auth.hashers import make_password, check_password
import re


def password_hash(password):
    return make_password(password)


def password_verify(password, hashed_password):
    return check_password(password, hashed_password) or password == hashed_password


def check_auth(session):
    if(session.get('role') == None or session.get('role') == ''):
        session.clear()
        session['role'] = ''
        session['user'] = ''


def check_phone_number(number, form):
    if not re.match(r'^\+37529\d{7}$', number):
        form.add_error(None, 'Phone must match the pattern: +37529XXXXXXX')


def validate_password_format(password, form):
    min_len = 5
    max_len = 32
    if len(password) < min_len or len(password) > max_len:
        form.add_error("Password's length must be between 5 and 32")
    elif not any(char.isdigit() for char in password):
        form.add_error("Password must contain at least 1 digit")
