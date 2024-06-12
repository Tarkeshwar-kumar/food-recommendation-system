import socket
import json

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 5000))

    print("WELCOME TO FOOD RECOMMENDATION APP")
    
    print("Please Login")

    user_id = input("Enter user id: ")
    password = input("Enter password: ")

    auth_request = {
        "user_id": user_id, 
        "password": password
    }


    auth_request_data = json.dumps(auth_request)

    client.sendall(bytes(auth_request_data,encoding="utf-8"))
    received = client.recv(1024)

print(received)