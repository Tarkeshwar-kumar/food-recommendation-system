from client.menu.menu import options
from client.controller.controller import User
import json
from client.utils.utils import show_recommendatio_table

class Chef(User):
    
    def display_options(self, client):
        for option in options['chef_options']:
            print(option, " -> ", options['chef_options'][option])

        self.choose_action(client)

    def roll_out_food_recommendation(self, client):
        try:
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
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            print(response['message'])
        finally:
            self.display_options(client)

    def get_food_recommendation(self, client, limit):
        try:
            request= {
                "request_type": "food_recommendation",
                "limit": limit
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            show_recommendatio_table(response)
        finally:
            self.display_options(client)

    def audit_foods(self, client):
        try:
            request= {
                "request_type": "audit_food",
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            show_recommendatio_table(response['message'])
        finally:
            self.display_options(client)

    def choose_action(self, client):
        action = input("Choose action: ")
        if action == "A":
            self.roll_out_food_recommendation(client)
        elif action == "B":
            self.view_menu(client)
        elif action == "C":
            limit = int(input("Enter number of food in recommendation: "))
            self.get_food_recommendation(client, limit)
        elif action == 'D':
            self.logout(client)
        elif action == "E":
            self.audit_foods(client)
        else:
            print("Invalid action")