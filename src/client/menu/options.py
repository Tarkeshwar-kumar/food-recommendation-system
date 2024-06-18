import json 
import socket
from getpass import getpass

class Auth:

    def authentication(client: socket.socket):
        user_id = input("Enter user id: ")
        password = getpass('Enter your password: ')

        auth_request = {
            "request_type": "auth",
            "user_id": user_id, 
            "password": password
        }
        auth_request_data = json.dumps(auth_request)

        client.sendall(bytes(auth_request_data,encoding="utf-8"))
        return client.recv(1024)