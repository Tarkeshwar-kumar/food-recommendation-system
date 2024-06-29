import socket
import json
import threading
from server.model.users import User
from server.model.user_factory import UserFactory
from server.db.db import DatabaseMethods
from typing import Any, Dict
from server.auth.auth import Auth

from server.utils.handler import *

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = None
        self.threads = []
        self.lock = threading.Lock()

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server listening on {self.host}:{self.port}")
        
        try:
            while True:
                conn, addr = self.server.accept()
                print(f"Connected by {addr}")
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                self.threads.append(thread)
        except Exception as e:
            print(f"Server exception: {e}")
        finally:
            self.stop_server()

    def handle_client(self, conn, addr):
        try:
            request_handler = RequestHandler(conn)
            request_handler.handle_requests()
        except Exception as e:
            print(f"Exception handling client {addr}: {e}")
        finally:
            conn.close()

    def stop_server(self):
        if self.server:
            print(self.threads)
            self.server.close()
        with self.lock:
            for thread in self.threads:
                thread.join()

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
                try:
                    json_data = json.loads(data)
                    print("Received:", json_data)
                    
                    if "request_type" not in json_data:
                        self.send_response({"status": "error", "message": "Missing request_type"})
                        continue

                    result = self.process_request(json_data)
                    self.send_response(result)
                except json.JSONDecodeError:
                    self.send_response({"status": "error", "message": "Invalid JSON"})
                except Exception as e:
                    self.send_response({"status": "error", "message": f"Server error: {str(e)}"})

    def process_request(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        if json_data["request_type"] == "auth":
            return self.handle_auth_request(json_data)
        else:
            return self.handle_other_requests(json_data)
        
    def handle_auth_request(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        auth = Auth()
        self.is_logged_in = False
        try:
            db = DatabaseMethods()
            role = db.authenticate(json_data['user_id'], json_data['password'])
            if role:
                self.user = UserFactory.create_user(json_data['user_id'])
                self.is_logged_in = True
                return {"status": "success", "isAuthenticated": True, "user": role}
            else:
                return {"status": "error", "message": "Authentication failed"}
        except ValueError as e:
            return {"status": "error", "message": str(e)}
        finally:
            auth.log_login_attempts(json_data['user_id'], self.is_logged_in)

    def handle_other_requests(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        if self.user is not None:
            return handle_request(self.user, json_data)
        else:
            return {"status": "error", "message": "User not authenticated"}

    def send_response(self, response: Dict[str, Any]):
        try:
            self.conn.sendall(json.dumps(response).encode("utf-8"))
            print("Response sent:", response)
        except Exception as e:
            print(f"Failed to send response: {e}")

def handle_request(user: User, json_data: Dict[str, Any]) -> Dict[str, Any]:
    request_type = json_data.get("request_type")
    handlers = {
        "display_menu": handle_display_menu,
        "add_item_to_menu": handle_add_item_to_menu,
        "change_food_price": handle_change_food_price,
        "change_food_availability": handle_change_food_availability,
        "remove_item_from_menu": handle_remove_item_from_menu,
        "give_feedback": handle_give_feedback,
        "vote": handle_vote,
        "rollout_recommendation": handle_rollout_recommendation,
        "food_recommendation": handle_food_recommendation,
        "check_notifications": handle_check_notification,
        "logout": handle_logout,
        "audit_food": handle_audit,
        "submit_improvement": handle_submit_improvement,
        "update_profile": handle_update_profile
    }

    if request_type in handlers:
        try:
            return handlers[request_type](user, json_data)
        except FoodAlreadyExists as e:
            return {"status": "error", "message": str(e)}
        except Exception as e:
            return {"status": "error", "message": f"An unexpected error occurred: Server Error {str(e)}"}
    else:
        return {"status": "error", "message": "Invalid request type"}

if __name__ == "__main__":
    server = Server("localhost", 5000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt, exiting")
    finally:
        server.stop_server()
