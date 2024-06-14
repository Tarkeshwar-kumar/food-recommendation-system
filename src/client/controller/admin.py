from client.menu.options import options
from client.controller.controller import User


class Admin(User):
    
    def display_options(self):
        for option in options['employee_options']:
            print(option)

        self.choose_action()

    def add_food_item_to_menu(self):
        pass

    def remove_food_item_from_menu(self):
        pass

    def change_food_item_price(self):
        pass

    def change_food_item_availability(self):
        pass

    def choose_action(self):
        pass