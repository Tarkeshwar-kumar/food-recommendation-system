import socket
import json
from client.menu.options import Auth
from client.controller.controller import User
from client.controller.employee import Employee
from client.controller.chef import Chef
from client.controller.admin import Admin
from client.exception.exceptions import NotAuthoriseError


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 5000))

    print("WELCOME TO FOOD RECOMMENDATION APP")
    print("Please Login")

    
    received = Auth.authentication(client)
    response = json.loads(received.decode().replace("'", '"'))
    print('r', response)
    if not response['isAuthenticated']:
        raise NotAuthoriseError(
            "You are not authorized to access app. Please contact admin."
        )
    if response['user'] == "Employee":
        user = Employee()
    elif response['user'] == 'Chef':
        user = Chef()
    else:
        user = Admin()

    user.display_options(client)
