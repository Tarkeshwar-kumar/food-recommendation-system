import mysql.connector
import os
from server.model.food import Food
from server.model.feedback import Feedback
from dotenv import load_dotenv


load_dotenv()
class DatabaseConnection:
   def __init__(self):
       self.host = "localhost"
       self.user = "root"
       self.password = os.getenv('PASSWORD')
       self.connection = None

   def __enter__(self):
       self.connection = mysql.connector.connect(
           host = self.host,
           user = self.user,
           password = self.password,
           database = "foodApp"
        )
       return self.connection

   def __exit__(self, exc_type, exc_value, traceback):
       if self.connection:
           self.connection.close()

class DatabaseMethods:

    def authenticate(self, user_id: str, password: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT * FROM User WHERE user_id='{user_id}' AND password='{password}';"""
            )
            response = cursor.fetchall()
            print(response)
            role = response[0][3]
            print(role)
            return role

    def get_user_details(self, user_id):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT user_id, user_name, role FROM User WHERE user_id='{user_id}';"""
            )
            response = cursor.fetchall()
            print(response)
            user_id, user_name, role = response[0][0], response[0][1], response[0][2]
            return user_id, user_name, role

    def insert_item_to_menu(self, food: Food):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO Food (food_name, price, availability_status, avg_rating, food_type, menu_id, spice_level, is_sweet, region) VALUES
                    ('{food.food_name}', {food.price}, {food.availability_status}, {food.avg_rating}, '{food.food_type}', 1, '{food.spice_level}', {food.is_sweet}, '{food.region}');
                """
            )
            connection.commit() 
            response = cursor.fetchall()
            print(response)
        
    def update_food_price(self, food_name: str, new_price: int):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    UPDATE Food SET price={new_price} WHERE food_name='{food_name}';
                """
            )
            connection.commit()
            print(response)

    def update_food_availability(self, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            
            # Retrieve the current availability status
            cursor.execute(
                """
                SELECT availability_status
                FROM Food
                WHERE food_name = %s;
                """,
                (food_name,)
            )
            result = cursor.fetchone()
            
            if result is not None:
                current_status = result[0]
                
                # Toggle the status
                new_availability = not current_status
                
                # Update the availability status
                cursor.execute(
                    """
                    UPDATE Food
                    SET availability_status = %s
                    WHERE food_name = %s;
                    """,
                    (new_availability, food_name)
                )
                connection.commit()
                print(f"Updated availability status of {food_name} to {new_availability}")
            else:
                print(f"Food item '{food_name}' not found.")

    def delete_item_from_menu(self, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f""" 
                    DELETE FROM Food WHERE food_name='{food_name}';

                """
            )
            connection.commit()
            response = cursor.fetchall()

    def insert_item_for_recommendation(self, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                """
                INSERT INTO RecommendedFood (food_name, total_vote)
                VALUES (%s, %s);
                """,
                (food_name, 0)
            )
            connection.commit() 
            response = cursor.fetchall()
            print(response)
            print("Item inserted successfully")

    def food_exists_in_menu(self, food_name) -> bool:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    SELECT * From Food WHERE food_name='{food_name}';
                """
            )
            response = cursor.fetchall()
            print(response)
            if len(response) > 0:
                return True
            return False
    
    def delete_table(self):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    DELETE FROM RecommendedFood;"
                """
            )

    def is_valid_feedback(self, food_name: str, user_id: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    SELECT * from Feedback WHERE food_name='{food_name}' and user_id='{user_id}';"
                """
            )
            response = cursor.fetchall()
            print(response)
            if len(response) == 0:
                return True
            return False

    def insert_into_feedback(self, feedback: Feedback):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            print("feedback", feedback)
            cursor.execute(
                """
                INSERT INTO Feedback (message, rating, sentiment, user_id, food_name)
                VALUES (%s, %s, %s, %s, %s);
                """,
                (feedback.comments, feedback.rating, feedback.sentiment, feedback.user_id, feedback.food_name)
            )
            connection.commit() 
            print("Item inserted successfully")

    def have_not_voted(self, user_id: str, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    SELECT * FROM Vote where user_id='{user_id}' and food_name='{food_name}';
                """
            )
            response = cursor.fetchall()
            print(response)
            if len(response) == 0:
                return True
            return False
        
    def vote_for_food_item(self, user_id: str, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                INSERT INTO Vote (user_id, have_voted, food_name) VALUES
                (%s, True, %s);
                """,
                (user_id, food_name)
            )
            connection.commit()
            self.increase_total_vote(food_name)

    def increase_total_vote(self, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE RecommendedFood
                SET total_vote = total_vote + 1
                WHERE food_name = %s;
                """,
                (food_name,)
            )
            connection.commit()
            print(f"Total vote for {food_name} increased by 1.")
        
    def display_menu(self):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    SELECT food_name, price, avg_rating FROM Food WHERE menu_id=1;
                """
            )
            print("    Food   ", "Price", "  Rating ")
            response = cursor.fetchall()
            print("res ", response)
            menu_details = [[]]
            for food_item in response:
                food = []
                food.append(food_item[0])
                food.append(str(food_item[1]))
                food.append(str(food_item[2]))
                print("food ", food)
                menu_details.append(food)

            return menu_details

    def get_epmloyee_list(self):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    SELECT user_id FROM User WHERE role='Employee';
                """
            )
            response = cursor.fetchall()
            user_id_list = []
            for user_id in response:
                user_id_list.append(user_id)

            return user_id_list
        
    def insert_notification(self, user_id, notification_type_id, food_name):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    INSERT INTO Notification (user_id, notification_type_id, Timestamp, food_name) 
                    VALUES (%s, %s, NOW(), %s)
                """,
                (user_id, notification_type_id, food_name)
            )
            connection.commit()

    def fetch_notifications_for_today(self, user_id: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                f"""
                    SELECT n.notification_id, nt.notification_type, n.food_name 
                    FROM Notification n
                    JOIN Notificationtype nt ON n.notification_type_id = nt.notification_type_id
                    WHERE n.user_id = %s AND DATE(n.Timestamp) = CURDATE();
                """,
                (user_id,)
            )
            notifications = cursor.fetchall()
            print("notifications ", notifications)
            return notifications

    def delete_notification(self, notification_id: int):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    DELETE FROM Notification 
                    WHERE notification_id = %s;
                """,
                (notification_id,)
            )
            connection.commit()

    def update_feedback(self, feedback: Feedback):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE Feedback
                SET message=%s, rating=%s, sentiment=%s
                WHERE user_id=%s AND food_name=%s;
                """,
                (feedback.comments, feedback.rating, feedback.sentiment, feedback.user_id, feedback.food_name)
            )
            connection.commit()
            print("Feedback updated successfully")

    def calculate_avg_rating(self, food_name):
        query = "SELECT AVG(rating) FROM Feedback WHERE food_name = %s"
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (food_name,))
            result = cursor.fetchone()
            return result[0] if result else 0
        
    def get_sentiment(self, food_name, sentiment_scores):
        query = "SELECT sentiment FROM Feedback WHERE food_name = %s"
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (food_name,))
            sentiments = cursor.fetchall()
            if not sentiments:
                return "Neutral"
            avg_score = sum(sentiment_scores[s[0]] for s in sentiments) / len(sentiments)
            if avg_score > 0:
                return "Positive"
            elif avg_score < 0:
                return "Negative"
            else:
                return "Neutral"
            
    def get_food_list(self):
        query = "SELECT food_name FROM Food"
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            food_names = [row[0] for row in cursor.fetchall()]
            return food_names

    def update_food_ratings(self, update_query, avg_rating, avg_sentiment, food_name):

        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(update_query, (avg_rating, avg_sentiment, food_name))
            conn.commit()

    def log_login_attempts(self, user_id, is_logged_in, attempt_type):
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    INSERT INTO LoginAttempts (user_id, attempt_type, status, Timestamp) VALUES
                    (%s, %s, %s, NOW())
                """,
                (user_id, attempt_type, is_logged_in)
            )
            conn.commit()

    def add_food_to_discard_menu(self, food_name, avg_rating):
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    INSERT INTO DiscardedFood (food_name, avg_rating) VALUES
                    (%s, %s)
                """,
                (food_name, avg_rating)
            )
            conn.commit()

    def update_profile(self, user_id: str, json_data):
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""
                    UPDATE User SET foodie_type ="{json_data['foodie_type']}", tooth_type = "{json_data['tooth_type']}",
                    spice_level = "{json_data['spice_level']}", preffered_type = "{json_data['preffered_type']}"
                    WHERE user_id = {user_id};             
                """,
            )
            conn.commit()


    def get_user_preferences(self, user_id):
        query = """
            SELECT spice_level, tooth_type, foodie_type, preffered_type 
            FROM User 
            WHERE user_id = %s
        """
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (user_id,))
            return cursor.fetchone()


    def get_food_list_for_user(self, user_preferences):
        print(user_preferences)
        query = """
            SELECT food_name 
            FROM Food 
            WHERE ((spice_level = %s) OR (spice_level IS NULL))
              AND ((food_type = %s) OR (food_type IS NULL))
              AND ((region = %s) OR (region IS NULL));
        """
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (
                user_preferences[0],
                user_preferences[2], 
                user_preferences[3],
            ))
            result = cursor.fetchall()
            print(result)
            return result
        
    def get_food_list(self):
        query = "SELECT food_name FROM Food"
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            food_names = [row[0] for row in cursor.fetchall()]
            return food_names
        
    def submit_food_audit_feedback(self, user_id, json_data):
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    INSERT INTO AuditFeedback (user_id, food_name, didnt_liked, like_to_taste, recipe) VALUES 
                    (%s, %s, %s, %s, %s)
                """,
                (user_id, json_data['food'], json_data['didnt_liked'], json_data['like_to_taste'], json_data['recipe'])
            )
            conn.commit()