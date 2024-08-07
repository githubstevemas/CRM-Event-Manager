from config.config import SessionFactory, global_db_session
from epic_events.controllers.auth_controller import register
from epic_events.models.employee import Employee
from epic_events.views.cli import display_register, display_employees


def get_employees():

    employees = SessionFactory.query(Employee).all()
    display_employees(employees)


def add_employee():

    new_employee = display_register()

    register(new_employee, global_db_session)


def edit_employee():

    print("edit employee")
    pass


def delete_employee():
    pass
