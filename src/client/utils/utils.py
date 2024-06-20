from prettytable import PrettyTable


def display_notifications(response):
    if response['status'] == 'success' and 'message' in response:
        notifications = response['message'].get('notifications', [])
        for notification in notifications:
            notification_type = notification['notification_type']
            food_name = notification['food_name']
            if notification_type == 'ADD_ITEM':
                print(f"{food_name} Added")
            elif notification_type == 'REMOVE_ITEM':
                print(f"{food_name} Removed")
    if len(notifications) == 0:
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