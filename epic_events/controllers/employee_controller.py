from argon2 import PasswordHasher

from config.config import global_db_session
from epic_events.controllers.auth_controller import register_employee
from epic_events.models.employee import Employee
from epic_events.views.cli import display_add_employee
from epic_events.views.reports import display_employees


ph = PasswordHasher()


def get_employees():

    employees = global_db_session.query(Employee).all()
    display_employees(employees)


def add_employee():

    new_employee = display_add_employee()
    register_employee(new_employee)

    print("Employee successfully added.")


def edit_employee():

    print("edit employee")
    pass
