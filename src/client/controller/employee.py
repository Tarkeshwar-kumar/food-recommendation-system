from client.menu.menu import options
from client.controller.controller import User
import json
from client.utils.utils import display_notifications
 
class Employee(User):
    
    def display_options(self, client):
        for option in options['employee_options']:
            print(option, " -> ", options['employee_options'][option])

        self.choose_action(client)

    def give_feedback_on_food(self, client):
        try:
            food_name = input("Enter food name: ")
            rating = float(input("How much you would rate this food: "))
            comment = input("What did you like ot disliked? ")

            request= {
                "request_type": "give_feedback",
                "food_name": food_name,
                "rating": rating,
                "comment": comment
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

    def vote_for_food_recommended_by_chef(self, client):
        try:
            food_name = input("Enter food name: ")
            request= {
                "request_type": "vote",
                "food_name": food_name
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

    def get_food_recommendation(self, client):
        try:
            request= {
                "request_type": "food_recommendation"
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

    def see_notification(self, client):
        try:
            request= {
                "request_type": "check_notifications"
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            display_notifications(response)
        finally:
            self.display_options(client)

    def choose_action(self, client):
        action = input("Choose action: ")
        if action == "A":
            self.give_feedback_on_food(client)
        elif action == "B":
            self.vote_for_food_recommended_by_chef(client)
        elif action == "C":
            self.view_menu(client)
        elif action == "D":
            self.see_notification(client)
        elif action == "E":
            self.get_food_recommendation(client)
        elif action == 'F':
            self.logout(client)
        else:
            print("Invalid action")