from config import session
from epic_events.controllers.auth_controller import register
from epic_events.models.client import Client
from epic_events.models.employee import Employee
from epic_events.views.cli import (display_employees,
                                   display_clients,
                                   display_main_menu,
                                   display_register)


def main_menu():

    choice = display_main_menu()
    if choice == "1":
        register_employee()
    elif choice == "2":
        get_employees()
    else:
        get_clients()


def register_employee():

    new_employee = display_register()
    register(new_employee[0],
             new_employee[1],
             new_employee[2],
             new_employee[3],
             new_employee[4],
             new_employee[5],
             new_employee[6])


def get_employees():

    employees = session.query(Employee).all()
    display_employees(employees)


def get_clients():

    clients = session.query(Client).all()
    display_clients(clients)
