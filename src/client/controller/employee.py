from client.menu.menu import options
from client.controller.controller import User
import json
from client.utils.utils import display_notifications, view_recommendation
from client.validation.validation import validate_profile


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
            limit = int(input("How many food items you want to see in recommendation"))
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
            view_recommendation(response)
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
            display_notifications(response, client)
        finally:
            self.display_options(client)

    def update_profile(self, client):
        try:
            foodie_type = input("Are you [Vegetarian/ Non Vegetarian/ Eggetarian]: ")
            spice_level = input("Please select your spice level [High/ Medium/ Low]: ")
            preffered_type = input("What do you prefer most [North Indian/ South Indian/ Other]: ")
            tooth_type = input("Do you have a sweet tooth [Yes/ No]: ")

            validate_profile(foodie_type, spice_level, preffered_type, tooth_type)

            request= {
                "request_type": "update_profile",
                "foodie_type": foodie_type,
                "spice_level": spice_level,
                "preffered_type": preffered_type,
                "tooth_type": tooth_type
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            print("User Profile updated Successfully !")
        finally:
            self.display_options(client)

    def give_improvement_feedback(self, client):
        try:
            
            request= {
                "request_type": "submit_improvement"
            }
            request_data = json.dumps(request)

            client.sendall(bytes(request_data,encoding="utf-8"))
            received = client.recv(1024)
            response = json.loads(received.decode().replace("'", '"'))
        except Exception as e:
            print(e)
        else:
            display_notifications(response, client)
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
        elif action == "G":
            self.update_profile(client)
        else:
            print("Invalid action")