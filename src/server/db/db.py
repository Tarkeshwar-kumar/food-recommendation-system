import mysql.connector
import os

class DatabaseConnection:
   def __init__(self):
       self.host = "localhost"
       self.user = os.environ("User")
       self.password = os.environ("PASSWORD")

   def __enter__(self):
       self.connection = mysql.connector.connect(
           host = self.host,
           user = self.user,
           password = self.password
        )
       return self.connection

   def __exit__(self, exc_type, exc_value, traceback):
       if self.connection:
           self.connection.close()