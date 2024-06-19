
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