from epic_events.controllers.validators import validate_password, \
    validate_email_adress, is_numeric, validate_datetime, get_employee_datas, \
    get_client_datas, get_contract_datas


def test_validate_password():

    wrong_password = "wrong"
    assert not validate_password(wrong_password)

    good_password = "Good@p4ssword"
    assert validate_password(good_password)


def test_validate_email():

    wrong_email = "wrong.email"
    assert not validate_email_adress(wrong_email)

    good_email = "good@email.com"
    assert validate_email_adress(good_email)


def test_is_numeric():

    wrong_input = "156stb16sr"
    assert not is_numeric(wrong_input)

    good_input = "1686.24"
    assert is_numeric(good_input)


def test_validate_datetime():

    wrong_input = "srthsrthwrth"
    assert not validate_datetime(wrong_input)

    good_input = "2024-12-31 15:30:00"
    assert validate_datetime(good_input)


def test_get_employee_datas(db_session):

    employee = get_employee_datas(1, db_session)
    assert employee.first_name == 'john'


def test_get_client_datas(db_session):

    client = get_client_datas(1, db_session)
    assert client.first_name == 'jane'


def test_get_contract_datas(db_session):

    contract = get_contract_datas(1, db_session)
    assert contract.left_to_pay == 500
