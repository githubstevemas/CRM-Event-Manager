from unittest.mock import patch

from epic_events.models import Employee
from epic_events.views.employee_view import get_department, \
    display_add_employee, display_ask_employee_to_edit
from epic_events.views.reports import display_employees


def test_get_department(capsys):

    with patch('builtins.input', return_value="1"):
        assert get_department() == "1"


def test_display_employees(db_session, insert_test_employee, capsys):

    insert_test_employee(email="branda@exemple.com", password="password123",
                         first_name="Branda", last_name="Daniels",
                         phone="1234567890",
                         role_id=2)

    employees = db_session.query(Employee).all()

    display_employees(employees)
    captured = capsys.readouterr()

    assert "Branda" in captured.out


def test_display_add_employee(db_session, capsys):

    with patch('epic_events.views.employee_view.get_department',
               return_value="2"):
        with patch('builtins.input', side_effect=['dan',
                                                  'willis',
                                                  'Password@123',
                                                  'dan@exemple.com',
                                                  '123456789']):

            new_test_employee = display_add_employee()

        assert new_test_employee['first_name'] == 'dan'


def test_display_ask_employee_to_edit(db_session, capsys):

    with patch('builtins.input', side_effect=['1', 'y']):

        employee_to_edit = display_ask_employee_to_edit()

        assert employee_to_edit.first_name == "michael"
