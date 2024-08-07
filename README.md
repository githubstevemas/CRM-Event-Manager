<br>

# CRM-Event-Manager
 
Python-based application designed to manage clients, events, and employees for your company. The application utilizes SQLAlchemy for database interactions and pytest for unit testing. The project includes features such as user authentication, role-based access control, and CRUD operations.

<br>

## Features

- **User Authentication:** Secure login system using hashed passwords and JWT tokens.
- **Role-Based Access Control:** Different menu options and permissions based on user roles (e.g., admin, support).
- **CRUD Operations:** Create, read, update, and delete clients and employees.

<br>

## Technologies used

- **[SQLAlchemy](https://www.sqlalchemy.org/)**: The main ORM library used for database interactions.
- **[pytest](https://pytest.org/)**: A framework used for testing the application.
- **[argon2](https://argon2-cffi.readthedocs.io/en/stable/)**: Used for hashing passwords securely.
- **[JWT (JSON Web Token)](https://jwt.io/)**: Used for handling authentication.
- **[psycopg2](https://www.psycopg.org/)**: PostgreSQL database adapter for Python.
- **[Python Dotenv](https://github.com/theskumar/python-dotenv)**: Used for managing environment variables.

<br>

## How to run
Once the code has been downloaded, go to the project directory and enter the following commands in terminal

*install all the depedencies :*
```
pip install -r requirements.txt
```

*define environment variables :*
```
python generate_dotenv.py
```

*set your ids in .env file :*
```
DB_PASSWORD=your_db_password
DB_USERNAME=your_db_username
```
<br>

> [!NOTE]
> The commands above are for Windows use. Go to the official [Python documentation](https://docs.python.org/3/tutorial/venv.html) for MacOS or Unix usage.

<br>

## Usage

*Run the application :*
```
python main.py your_email
```
<br>

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
