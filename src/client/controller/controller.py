from client.menu.options import options

class User:
    user_id: str
    role: str

    def __init__(self):
        self.user_id = "user-id"
        self.role = "role"

    def display_options():
        pass
    
class Employee(User):
    
    def display_options():
        for option in options['user_option']:
            print(option)

class Chef(User):
    
    def display_options():
        for option in options['chef_options']:
            print(option)

class Admin(User):
    
    def display_options():
        for option in options['employee_options']:
            print(option)