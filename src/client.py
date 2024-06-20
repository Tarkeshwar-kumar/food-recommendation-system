import socket
import json
from client.menu.options import Auth
from client.controller.controller import User
from client.controller.employee import Employee
from client.controller.chef import Chef
from client.controller.admin import Admin
from client.exception.exceptions import NotAuthoriseError
import getpass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 5000))

    print("WELCOME TO FOOD RECOMMENDATION APP")
    print("Please Login")

    
    received = Auth.authentication(client)
    response = json.loads(received.decode().replace("'", '"'))

    if response['status'] == "success":
        user_type = response['user']
        if user_type == "Employee":
            user = Employee()
        elif user_type == "Chef":
            user = Chef()
        else:
            user = Admin()

        user.display_options(client)
    else:
        print("Authentication failed or unauthorized access")