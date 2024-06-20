import json


class User:
    user_id: str
    role: str

    def __init__(self):
        self.user_id = "user-id"
        self.role = "role"

    def display_options(self):
        pass

    def logout(self, client):
        try:
            request = {
                "request_type" : "logout"
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))

        except Exception as e:
            print("what", e)
        else:
            if response.get('status') == "success":
                print("Logging out")
                exit(1)

    def view_menu(self, client):
        try:
            request = {
                "request_type" : "display_menu"
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))

        except Exception as e:
            print("what", e)
        else:
            if response.get('status') == "success":
                print(type(response['message']))
                for item in response['message']:
                    print("  Name  ", "  Price   ", "  Rating  ")
                    if item:  
                        name, price, rating = item
                        print(f"  {name}  {price}  {rating}")        
        finally:
            self.display_options(client)

    def choose_action(self):
        pass
   