import json


class User:
    user_id: str
    role: str

    def __init__(self):
        self.user_id = "user-id"
        self.role = "role"

    def display_options(self):
        pass

    def view_menu(self, client):
        request = {
            "request_type" : "display_menu"
        }
        request_data = json.dumps(request)

        client.sendall(bytes(request_data,encoding="utf-8"))
        print(client.recv(1024))

    def choose_action(self):
        pass
   