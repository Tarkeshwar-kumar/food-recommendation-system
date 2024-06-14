from client.menu.options import options
from client.controller.controller import User

 
class Employee(User):
    
    def display_options(self):
        for option in options['user_option']:
            print(option)

        self.choose_action()

    def give_feedback_on_food(self):
        pass

    def vote_for_food_recommended_by_chef(self):
        pass

    def choose_action(self):
        pass