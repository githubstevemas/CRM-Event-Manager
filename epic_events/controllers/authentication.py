from datetime import datetime, timedelta, timezone

import jwt

from argon2 import PasswordHasher
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from sqlalchemy.orm import Session
from cryptography.hazmat.primitives.serialization import load_pem_private_key, \
    load_pem_public_key

from epic_events.models.employee import Employee
from config import session
from epic_events.models.token import Token

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


def is_email_exists(email):
    exists_query = session.query(Employee.id).filter_by(email=email).exists()
    result = session.query(exists_query).scalar()

    return result


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

    payload = {
        'user_id': employee_email,
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(payload, private_key, algorithm='RS256')
    save_token_to_db(employee_email, token)


def save_token_to_db(employee_email, token):

    employee = session.query(Employee).filter_by(email=employee_email).first()
    new_token = Token(token=token, employee_id=employee.id)
    session.add(new_token)
    session.commit()
