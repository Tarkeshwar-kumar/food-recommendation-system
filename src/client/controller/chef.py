from client.menu.options import options
from client.controller.controller import User

class Chef(User):
    
    def display_options(self):
        for option in options['chef_options']:
            print(option)

        self.choose_action()

    def roll_out_food_recommendation(self):
        pass

    def choose_action(self):
        pass