from tabulate import tabulate


def display_employees(employees_list):
    headers = ["First name", "Last name", "Email", "Phone", "Role"]
    datas = [[employee.first_name, employee.last_name, employee.email,
              employee.phone, employee.role.name] for employee in
             employees_list]

    table = tabulate(datas, headers=headers, tablefmt="rounded_grid",
                     numalign="center", stralign="center")
    print(table)


def display_clients(clients_list):
    headers = ["First name", "Last name", "Email", "Phone", "Company",
               "First contact", "Commercial"]
    datas = [[client.first_name, client.last_name, client.email,
              client.phone, client.company_name, client.first_contact,
              client.commercial.last_name]
             for
             client in
             clients_list]

    table = tabulate(datas, headers=headers, tablefmt="rounded_grid",
                     numalign="center", stralign="center")
    print(table)


def display_contracts(contracts_list):
    headers = ["Reference", "Client", "Commercial", "Amount ($)",
               "Left to Pay ($)", "Creation", "Status"]
    datas = [
        [contract.id, contract.client.last_name, contract.commercial.last_name,
         contract.amount,
         contract.left_to_pay, contract.contract_creation_date,
         contract.status] for
        contract in contracts_list]

    table = tabulate(datas, headers=headers, tablefmt="rounded_grid",
                     numalign="center", stralign="center")
    print(table)


def display_events(events_list):
    headers = ["Reference", "Client", "Start date", "End date", "Support",
               "Location", "Attendees", "Notes"]
    datas = [
        [event.contract_id, event.client.last_name, event.event_date_start,
         event.event_date_end, event.support.last_name, event.location,
         event.attendees, event.notes] for
        event in
        events_list]

    table = tabulate(datas, headers=headers, tablefmt="rounded_grid",
                     numalign="center", stralign="center")
    print(table)
