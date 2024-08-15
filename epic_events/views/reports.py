from rich.console import Console
from rich.table import Table

console = Console()


def display_employees(employees_list):
    table = Table(title="Employees")

    table.add_column("Id", justify="center", style="cyan")
    table.add_column("First name", justify="center", style="cyan")
    table.add_column("Last name", justify="center", style="cyan")
    table.add_column("Email", justify="center", style="cyan")
    table.add_column("Phone", justify="center", style="cyan")
    table.add_column("Role", justify="center", style="cyan")

    for employee in employees_list:
        table.add_row(
            str(employee.id),
            employee.first_name,
            employee.last_name,
            employee.email,
            employee.phone,
            employee.role.name
        )

    console.print(table)


def display_clients(clients_list):
    table = Table(title="Clients")

    table.add_column("Id", justify="center", style="cyan")
    table.add_column("First name", justify="center", style="cyan")
    table.add_column("Last name", justify="center", style="cyan")
    table.add_column("Email", justify="center", style="cyan")
    table.add_column("Phone", justify="center", style="cyan")
    table.add_column("Company", justify="center", style="cyan")
    table.add_column("First contact", justify="center", style="cyan")
    table.add_column("Commercial", justify="center", style="cyan")

    for client in clients_list:
        table.add_row(
            str(client.id),
            client.first_name,
            client.last_name,
            client.email,
            client.phone,
            client.company_name,
            str(client.first_contact),
            client.commercial.last_name
        )

    console.print(table)


def display_contracts(contracts_list):
    table = Table(title="Contracts")

    table.add_column("Reference", justify="center", style="cyan")
    table.add_column("Client", justify="center", style="cyan")
    table.add_column("Commercial", justify="center", style="cyan")
    table.add_column("Amount", justify="right", style="cyan")
    table.add_column("Left to Pay", justify="right", style="cyan")
    table.add_column("Creation", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="cyan")

    for contract in contracts_list:
        table.add_row(
            str(contract.id),
            contract.client.last_name,
            contract.commercial.last_name,
            f"${contract.amount:,.2f}",
            f"${contract.left_to_pay:,.2f}",
            str(contract.contract_creation_date),
            "Signed" if contract.status else "Not signed"
        )

    console.print(table)


def display_events(events_list):
    table = Table(title="Events")

    table.add_column("Reference", justify="center", style="cyan")
    table.add_column("Client", justify="center", style="cyan")
    table.add_column("Start date", justify="center", style="cyan")
    table.add_column("End date", justify="center", style="cyan")
    table.add_column("Support", justify="center", style="cyan")
    table.add_column("Location", justify="center", style="cyan")
    table.add_column("Attendees", justify="center", style="cyan")
    table.add_column("Notes", justify="center", style="cyan")

    for event in events_list:
        table.add_row(
            str(event.contract_id),
            event.client.last_name,
            str(event.event_date_start),
            str(event.event_date_end),
            event.support.last_name,
            event.location,
            str(event.attendees),
            event.notes
        )

    console.print(table)
