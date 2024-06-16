import socket
import json
from server.model.users import User, Admin, Employee, Chef
from server.model.user_factory import UserFactory
from server.db.db import DatabaseMethods
from typing import Any, Dict, Tuple
from server.model.food import Food

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.conn = None
        self.addr = None
        self.server = None

    def start_server(self) -> Tuple[Any, Any, Any]:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 5000))
        server.listen()
        print("Server listening on port 5000")
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        return conn, addr, server

    def stop_server(self):
        if self.conn:
            self.conn.close()
        if self.server:
            self.server.close()

class RequestHandler:
    def __init__(self, connection: Any):
        self.conn = connection
        self.user: User = None

    def handle_requests(self):
        with self.conn:
            while True:
                data = self.conn.recv(1024).decode("utf-8")
                if not data:
                    break
                json_data = json.loads(data)
                print("Received:", json_data)

                if "request_type" not in json_data:
                    continue

                response = self.process_request(json_data)
                self.conn.sendall(json.dumps(response).encode("utf-8"))

    def process_request(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        if json_data["request_type"] == "auth":
            return self.handle_auth(json_data)
        else:
            return self.handle_other_requests(json_data)
        
    def handle_auth(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        db = DatabaseMethods()
        role = db.authenticate(json_data['user_id'], json_data['password'])
        if role:
            try:
                self.user = UserFactory.create_user(json_data['user_id'])
                return {"status": "success", "isAuthenticated": True, "user": role}
            except ValueError as e:
                return {"status": "error", "message": str(e)}
        else:
            return {"status": "error", "message": "Authentication failed"}
        
    def handle_other_requests(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        if self.user is not None:
            return handle_request(self.user, json_data)
        else:
            return {"status": "error", "message": "User not authenticated"}

def handle_request(user: User, json_data):
    request_type = json_data["request_type"]
    if request_type == "display_menu":
        return user.display_menu()
    elif request_type == "add_item_to_menu":
        food = Food(
            food_name=json_data["food_name"],
            price= json_data["price"],
            availability_status = True,
            category= json_data["food_type"],
            avg_rating=0,
            feedbacks=[],
            food_type=json_data["food_type"]
        )
        return user.add_item_to_menu(food)
    elif request_type == "change_food_price":
        return user.change_food_price(json_data["food_name"], json_data["new_price"])
    elif request_type == "change_food_availability":
        return user.change_food_availability(json_data["new_price"], json_data["availability"])
    elif request_type == "remove_item_from_menu":
        return user.remove_item_from_menu(json_data["new_price"])
    elif request_type == "give_feedback":
        return user.give_feedback(json_data["item_id"], json_data["feedback"])
    elif request_type == "vote":
        return user.vote_food_recommended(json_data["item_id"], json_data["feedback"])
    elif request_type == "rollout_recommendation":
        return user.rollout_food_recommendation(json_data["recommended_food"], json_data["feedback"])
    else:
        return {"status": "error", "message": "Invalid request"}


if __name__ == "__main__":
    server = Server("localhost", 8000)
    try:
        conn, addr, server_instance = server.start_server()
        server.conn = conn
        server.addr = addr
        server.server = server_instance

        request_handler = RequestHandler(conn)
        request_handler.handle_requests()

    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt, exiting")
    finally:
        server.stop_server()