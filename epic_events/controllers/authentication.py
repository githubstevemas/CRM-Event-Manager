from argon2 import PasswordHasher, exceptions
from sqlalchemy.orm import Session

from epic_events.models.employee import Employee

ph = PasswordHasher()


def hash_password(password):
    # Return an hashed and salted password with argon2
    return ph.hash(password)


def register(first_name: str,
             last_name: str,
             password: str,
             email: str,
             phone: str,
             department: str,
             db: Session):

    # Hash & salt password and create Employee instance
    hashed_password = hash_password(password)
    new_employee = Employee(first_name=first_name,
                            last_name=last_name,
                            password=hashed_password,
                            email=email,
                            phone=phone,
                            department=department)

    # Add new_employee to the db
    db.add(new_employee)
    db.commit()
    return new_employee
