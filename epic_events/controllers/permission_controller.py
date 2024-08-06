import jwt

from config.config import global_db_session as session
from config.keys import get_public_key
from epic_events.models.employee import Employee

TOKEN_PATH = 'tokens/token.txt'


def load_token():
    # Load token from local txt and return it

    with open('tokens/token.txt', 'r') as file:
        token = file.read()
    return token


def verify_token(path=TOKEN_PATH):
    with open(path) as file:
        token = file.read()

    public_key = get_public_key()

    try:
        payload = jwt.decode(token, public_key, algorithms=["RS256"])
        print(f"token OK. {payload}")
        return payload
    except jwt.ExpiredSignatureError:
        print("Old token.")
        return False
    except jwt.InvalidTokenError:
        print("Wrong token.")
        return False


def verify_role(payload):
    employee = session.query(Employee).filter_by(
        email=payload['user_id']).first()

    role = employee.role_id
    return role
