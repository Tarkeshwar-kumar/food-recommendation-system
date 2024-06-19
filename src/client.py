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

    if response['status'] != "success":
        print(
            "You are not authorized to access app. Please contact admin."
        )
    else:   
        if response['message'] == "Employee":
            user = Employee()
        elif response['message'] == 'Chef':
            user = Chef()
        else:
            user = Admin()

        user.display_options(client)
