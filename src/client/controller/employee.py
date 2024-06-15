from client.menu.menu import options
from client.controller.controller import User

 
class Employee(User):
    
    def display_options(self):
        for option in options['employee_options']:
            print(option, " -> ", options[option])

        self.choose_action()

    def give_feedback_on_food(self):
        request= {
            "request_type": ""
        }

    def vote_for_food_recommended_by_chef(self):
        request= {
            "request_type": ""
        }

    def choose_action(self):
        action = input("Choose action: ")
        if action == "A":
            self.give_feedback_on_food()
        elif action == "B":
            self.vote_for_food_recommended_by_chef()
        elif action == "C":
            self.view_menu()
        else:
            print("Invalid action")