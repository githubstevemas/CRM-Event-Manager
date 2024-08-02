import os
from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key
)
from sqlalchemy.orm import Session

from config import session
from epic_events.models.employee import Employee
from epic_events.views.cli import ask_password


ph = PasswordHasher()


def hash_password(password):
    # Return hashed and salted password with argon2

    return ph.hash(password)


def register(first_name: str,
             last_name: str,
             password: str,
             email: str,
             phone: str,
             role_id: str,
             db: Session):

    # Hash & salt password and create Employee instance
    hashed_password = hash_password(password)

    new_employee = Employee(first_name=first_name,
                            last_name=last_name,
                            password=hashed_password,
                            email=email,
                            phone=phone,
                            role_id=role_id)

    # Add new_employee to the db
    db.add(new_employee)
    db.commit()
    return new_employee


def main_login(args):

    exists = is_email_exists(args.email)

    # if email in db ask for password
    if exists:

        password = ask_password()
        if verify_password(password, args.email):

            # if password OK get encrypted token and save it
            token = create_encrypted_token(args.email)
            save_token(token)

        else:
            print("password NOK")

    else:
        print("Wrong email.")


def is_email_exists(email):

    exists_query = session.query(Employee.id).filter_by(email=email).exists()
    result = session.query(exists_query).scalar()

    return result


def verify_password(provided_password, email):

    employee = session.query(Employee).filter_by(email=email).first()

    stored_password = employee.password
    # print(stored_password)

    return ph.verify(stored_password, provided_password)


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

private_key = load_pem_private_key(private_pem, password=None)
public_key = load_pem_public_key(public_key)


def create_encrypted_token(employee_email):
    # Put employee_email in playload and sign token

    payload = {
        'user_id': employee_email,
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(payload, private_key, algorithm='RS256')

    return token


def save_token(token):
    # With signed token, save it on local

    folder = 'tokens'
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, 'token.txt')

    with open(filepath, 'w') as file:
        file.write(token)


def load_token():
    # Load token from local txt and return it

    with open('tokens/token.txt', 'r') as file:
        token = file.read()
    return token
