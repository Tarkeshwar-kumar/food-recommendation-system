import mysql.connector as sql

conn = sql.connect(
  host="localhost",
  user="root",
  password="chelsiGoyal@123",
  database="foodApp"
)

class Auth:
    def authenticate(user_id: str, password: str):
        if user_id == "user_id" and password == "password":
            return True
        return False