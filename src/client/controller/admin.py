from client.menu.menu import options
from client.controller.controller import User
import json

class Admin(User):
    
    def display_options(self, client):
        for option in options['admin_options']:
            print(option, " -> ", options['admin_options'][option])

        self.choose_action(client)

    def add_food_item_to_menu(self, client):
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
        print(client.recv(1024))

    def remove_food_item_from_menu(self, client):
        request= {
            "request_type": ""
        }

    def change_food_item_price(self, client):
        request= {
            "request_type": ""
        }

    def change_food_item_availability(self, client):
        request= {
            "request_type": ""
        }

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