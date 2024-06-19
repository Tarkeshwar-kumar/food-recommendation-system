from client.menu.menu import options
from client.controller.controller import User
import json

class Admin(User):

    def display_options(self, client):
        for option in options['admin_options']:
            print(option, " -> ", options['admin_options'][option])

        self.choose_action(client)

    def add_food_item_to_menu(self, client):
        try:    
            food_name = input("Enter food name: ")
            price = float(input("Enter food price: "))
            type = input("Enter food type: ")
            request= {
                "request_type": "add_item_to_menu",
                "food_name": food_name,
                "price": price,
                "food_type": type
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            if response.get('status') == "success":
                print("Food added successfully")
            else:
                print(response['message'])
        finally:
            self.display_options(client)
        
        
    def remove_food_item_from_menu(self, client):
        try:
            food_name = input("Enter food name: ")

            if not food_name:
                raise ValueError("Food name cannot be empty.")
        
            request = {
                "request_type": "remove_item_from_menu",
                "food_name": food_name
            }
            request_data = json.dumps(request)
        
            client.sendall(bytes(request_data, encoding="utf-8"))
        
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
                
        except Exception as e:
            print(e)
        else:
            if response.get('status') == "success":
                print("Food removed successfully")
            else:
                print(response['message'])
        finally:
            self.display_options(client)


    def change_food_item_price(self, client):
        try:
            food_name = input("Enter food name: ")
            price = float(input("Enter food price: "))
            request= {
                "request_type": "change_food_price",
                "food_name": food_name,
                "new_price": price
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
                
        except Exception as e:
            print(e)
        else:
            if response.get('status') == "success":
                print("Food price updated successfully")
            else:
                print(response['message'])
        finally:
            self.display_options(client)

    def change_food_item_availability(self, client):
        try:
            food_name = input("Enter food name: ")
            availability = float(input("Is food available?: "))
            availability = True if availability=="Yes" else False
            request= {
                "request_type": "change_food_availability",
                "food_name": food_name,
                "availability": availability
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
                
        except Exception as e:
            print(e)
        else:
            if response.get('status') == "success":
                print("Food item price changed successfully")
            else:
                print(response['message'])
        finally:
            self.display_options(client)

    def choose_action(self, client):
        action = input("Choose action: ")
        if action == "A":
            self.add_food_item_to_menu(client)
        elif action == "B":
            self.remove_food_item_from_menu(client)
        elif action == "C":
            self.change_food_item_price(client)
        elif action == "D":
            self.change_food_item_availability(client)
        elif action == "E":
            self.view_menu(client)
        else:
            print("Invalid action")