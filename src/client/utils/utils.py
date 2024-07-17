from prettytable import PrettyTable
import json


def display_notifications(response, client):
    if response.get('notifications'):
        notifications = response.get('notifications', [])
        for notification in notifications:
            notification_type = notification['notification_type']
            food_name = notification['food_name']
            if notification_type == 'ADD_ITEM':
                print(f"{food_name} Added")
            elif notification_type == 'REMOVE_ITEM':
                print(f"{food_name} Removed")
            elif notification_type == 'FOOD_AVAILABILITY_CHANGED':
                print(f"{food_name} AVAILABILITY CHANGED")
            elif notification_type == "FOOD_AUDIT":
                submit_improvement_feedback(food_name, client)
    else:
        print("No new notifications")

def show_recommendatio_table(data):
    table = PrettyTable(['Food', 'Rating'])

    for row in data:
        table.add_row(row)

    table.align['Food'] = 'l'  
    table.align['Rating'] = 'r' 

    print(table)

def show_menu(data):
    table = PrettyTable(['Food', 'Price', 'Rating'])
    for item in data:
        if item and len(item) >= 3:
            name, price, rating = item[:3]
            table.add_row([name, price, rating])
        else:
            print(f"Invalid menu item format: {item}")
    table.align['Food'] = 'l'
    table.align['Price'] = 'r'
    table.align['Rating'] = 'r'
    print(table)

def submit_improvement_feedback(food_name, client):
    try:
        didnt_liked = input(f"What didn’t you like about {food_name}? ")
        like_to_taste = input(f"How would you like {food_name} to taste? ")
        recipe = input(f"Share you own recipe: ")

        request= {
                "request_type": "submit_improvement",
                "didnt_liked": didnt_liked,
                "like_to_taste" : like_to_taste,
                "recipe" : recipe,
                "food": food_name
        }
        request_data = json.dumps(request)

        client.sendall(bytes(request_data,encoding="utf-8"))
        received = client.recv(1024)
        response = json.loads(received.decode().replace("'", '"'))
    except Exception as e:
        print(e)
    else:
        print(response)

def view_recommendation(response):
    table = PrettyTable(['Food', 'Rating'])

    for item in response:
        if item and len(item) >= 2:
            name, rating = item[:2]
            table.add_row([name, rating])
        else:
            print(f"Invalid menu item format: {item}")
    table.align['Food'] = 'l'
    table.align['Rating'] = 'r'
    print(table)

