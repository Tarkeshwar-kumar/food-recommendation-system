from client.menu.menu import options
from client.controller.controller import User
import json


class Chef(User):
    
    def display_options(self, client):
        for option in options['chef_options']:
            print(option, " -> ", options['chef_options'][option])

        self.choose_action(client)

    def roll_out_food_recommendation(self, client):
        number_of_items = int(input("Enter number of items: "))
        list_of_food = []
        for _ in range(number_of_items):
            food_name = input("Enter food name: ")
            list_of_food.append(food_name)
        request= {
            "request_type": "rollout_recommendation",
            "recommended_food": list_of_food
        }
        request_data = json.dumps(request)

        client.sendall(bytes(request_data,encoding="utf-8"))
        print(client.recv(1024))

    def choose_action(self, client):
        action = input("Choose action: ")
        if action == "A":
            self.roll_out_food_recommendation(client)
        elif action == "B":
            self.view_menu()
        else:
            print("Invalid action")