import os
import sys
from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.orm import Session

from config.config import global_db_session as session
from config.keys import get_private_key
from epic_events.controllers.permission_controller import verify_token
from epic_events.models.employee import Employee
from epic_events.views.cli import ask_password

TOKEN_PATH = 'tokens/token.txt'
ph = PasswordHasher()


def hash_password(password):
    # Return hashed and salted password with argon2

    return ph.hash(password)


def register(new_employee, db: Session):
    # Hash & salt password and create Employee instance
    hashed_password = hash_password(new_employee['password'])

    new_employee = Employee(first_name=new_employee['first_name'],
                            last_name=new_employee['last_name'],
                            password=hashed_password,
                            email=new_employee['email'],
                            phone=new_employee['phone'],
                            role_id=new_employee['role_id'])

    # Add new_employee to the db
    db.add(new_employee)
    db.commit()
    return new_employee


def main_login(args):
    exists = is_email_exists(args.email, session)

    # if email in db ask for password
    if exists:

        try_nb = 2

        while True:

            password = ask_password()

            if verify_password(password, args.email, session):
                # if password OK get encrypted token and save it
                token = create_encrypted_token(args.email)
                save_token(token)
                break

            else:
                if try_nb == 0:
                    sys.exit()

                print(f"password NOK. {try_nb} attempts left.")
                try_nb -= 1

    else:
        print("Email not in db.")
        sys.exit()


def logout():

    payload = verify_token()
    if payload:
        employee = session.query(Employee).filter_by(
            email=payload['user_id']).first()

        employee.is_logged_in = False
        session.commit()

    os.remove(TOKEN_PATH)
    print("You are now deconnected.")
    sys.exit()


def is_email_exists(email, session):

    employee = session.query(Employee.id).filter_by(email=email).exists()
    result = session.query(employee).scalar()
    return result


def verify_password(provided_password, email, session):

    employee = session.query(Employee).filter_by(email=email).first()
    stored_password = employee.password

    try:
        return ph.verify(stored_password, provided_password)
    except VerifyMismatchError:
        return False


def create_encrypted_token(employee_email):
    # Put employee_email in playload and sign token

    private_key = get_private_key()

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

    with open(TOKEN_PATH, 'w') as file:
        file.write(token)
