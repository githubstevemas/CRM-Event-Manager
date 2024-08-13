from validate_email import validate_email
from password_validator import PasswordValidator

from config.config import global_db_session as session
from epic_events.controllers.permission_controller import verify_token
from epic_events.models import Employee, Client, Contract


def validate_password(password):

    schema = PasswordValidator()

    schema \
        .min(8) \
        .max(100) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().no().spaces() \
        .has().symbols()

    return schema.validate(password)


def validate_email_adress(email):
    return validate_email(email)


def get_employee_id():

    payload = verify_token()
    if payload:
        employee = session.query(Employee).filter_by(
            email=payload['user_id']).first()

        return employee.id


def get_employee_datas(employee_id, global_db_session=session):

    employee = global_db_session.query(Employee).filter_by(
        id=employee_id).first()

    return employee


def get_client_datas(client_id, global_db_session=session):

    client = global_db_session.query(Client).filter_by(id=client_id).first()

    return client


def get_contract_datas(contract_id, global_db_session=session):

    contract = global_db_session.query(Contract).filter_by(
        id=contract_id).first()

    return contract


def get_event_datas(event_id, global_db_session=session):

    pass
