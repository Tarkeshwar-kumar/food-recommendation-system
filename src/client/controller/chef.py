from client.menu.menu import options
from client.controller.controller import User

class Chef(User):
    
    def display_options(self):
        for option in options['chef_options']:
            print(option, " -> ", options[option])

        self.choose_action()

    def roll_out_food_recommendation(self):
        request= {
            "request_type": ""
        }

    def choose_action(self):
        action = input("Choose action: ")
        if action == "A":
            self.roll_out_food_recommendation()
        elif action == "B":
            self.view_menu()
        else:
            print("Invalid action")