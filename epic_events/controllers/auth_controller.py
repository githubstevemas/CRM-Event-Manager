import os
from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher
from sqlalchemy.orm import Session

from config.config import global_db_session as session
from config.keys import get_private_key
from epic_events.models.employee import Employee
from epic_events.views.cli import ask_password


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

        password = ask_password()
        if verify_password(password, args.email):

            # if password OK get encrypted token and save it
            token = create_encrypted_token(args.email)
            save_token(token)

        else:
            print("password NOK")

    else:
        print("Wrong email.")


def logout():
    pass


def is_email_exists(email, session):

    exists_query = session.query(Employee.id).filter_by(email=email).exists()
    result = session.query(exists_query).scalar()
    return result


def verify_password(provided_password, email):

    employee = session.query(Employee).filter_by(email=email).first()

    stored_password = employee.password
    # print(stored_password)

    return ph.verify(stored_password, provided_password)


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
    filepath = os.path.join(folder, 'token.txt')

    with open(filepath, 'w') as file:
        file.write(token)


def load_token():
    # Load token from local txt and return it

    with open('tokens/token.txt', 'r') as file:
        token = file.read()
    return token
