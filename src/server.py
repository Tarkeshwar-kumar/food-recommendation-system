import socket
import json
from server.auth.auth import Auth


def start_server():
    server.bind(("localhost", 5000))
    server.listen()
    conn, addr = server.accept()

    return conn, addr

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    
    conn, addr = start_server()

    with conn:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            json_data = json.loads(data)
            if json_data["request_type"] == "auth":
                auth = Auth()
                if (auth.authenticate(json_data['user_id'], json_data['password'])):
                    print("Authenticated")