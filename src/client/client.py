import socket
import json
from client.menu.options import Auth
from client.controller.controller import User, Employee, Chef, Admin


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 5000))

    print("WELCOME TO FOOD RECOMMENDATION APP")
    print("Please Login")

    
    received = Auth.authentication()
    
    if not received['isAuthenticated']:
        raise Exception
    if received['user'] == "Employee":
        user = Employee()
    elif received['user'] == 'Chef':
        user = Chef()
    else:
        user = Admin()

    user.display_options()
