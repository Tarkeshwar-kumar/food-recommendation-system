from client.menu.menu import options
from client.controller.controller import User
import json
 
class Employee(User):
    
    def display_options(self, client):
        for option in options['employee_options']:
            print(option, " -> ", options['employee_options'][option])

        self.choose_action(client)

    def give_feedback_on_food(self, client):
        food_name = input("Enter food name: ")
        rating = float(input("How much you would rate this food: "))
        comment = input("What did you like ot disliked? ")
        is_liked = input("Did you like the food? ")
        request= {
            "request_type": "give_feedback",
            "food_name": food_name,
            "rating": rating,
            "comment": comment,
            "is_liked": is_liked
        }
        request_data = json.dumps(request)

        client.sendall(bytes(request_data,encoding="utf-8"))
        print(client.recv(1024))

    def vote_for_food_recommended_by_chef(self, client):
        food_name = input("Enter food name: ")
        request= {
            "request_type": "vote",
            "food_name": food_name
        }
        request_data = json.dumps(request)

        client.sendall(bytes(request_data,encoding="utf-8"))
        print(client.recv(1024))


    def choose_action(self, client):
        action = input("Choose action: ")
        if action == "A":
            self.give_feedback_on_food(client)
        elif action == "B":
            self.vote_for_food_recommended_by_chef(client)
        elif action == "C":
            self.view_menu(client)
        else:
            print("Invalid action")