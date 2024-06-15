import socket
import json
from server.model.users import User, Admin, Employee, Chef
from server.model.user_factory import UserFactory
from server.db.db import DatabaseMethods

def handle_request(user, json_data):
    request_type = json_data["request_type"]
    if request_type == "display_menu":
        return user.display_menu()
    elif request_type == "add_item_to_menu":
        return user.add_item_to_menu(json_data["item"])
    elif request_type == "change_food_price":
        return user.change_food_price(json_data["item_id"], json_data["new_price"])
    elif request_type == "change_food_availability":
        return user.change_food_availability(json_data["item_id"], json_data["availability"])
    elif request_type == "remove_item_from_menu":
        return user.remove_item_from_menu(json_data["item_id"])
    elif request_type == "give_feedback":
        return user.give_feedback(json_data["item_id"], json_data["feedback"])
    elif request_type == "vote":
        return user.vote_food_recommended(json_data["item_id"], json_data["feedback"])
    elif request_type == "rollout_recommendation":
        return user.rollout_food_recommendation(json_data["item_id"], json_data["feedback"])
    else:
        return {"status": "error", "message": "Invalid request"}

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen()
    print("Server listening on port 5000")
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    return conn, addr, server

if __name__ == "__main__":
    conn = None
    server = None
    try:
        conn, addr, server = start_server()
        user = None
        with conn:
            while True:
                data = conn.recv(1024).decode("utf-8")
                if not data:
                    break
                json_data = json.loads(data)
                print("Received:", json_data)

                if "request_type" not in json_data:
                    continue

                if json_data["request_type"] == "auth":
                    db = DatabaseMethods()
                    role = db.authenticate(json_data['user_id'], json_data['password'])
                    if role:
                        try:
                            user = UserFactory.create_user(json_data['user_id'])
                            response = {
                                "status": "success", 
                                "isAuthenticated": True,
                                "user": role
                            }
                            conn.sendall(json.dumps(response).encode("utf-8"))
                        except ValueError as e:
                            response = {"status": "error", "message": str(e)}
                    else:
                        response = {"status": "error", "message": "Authentication failed"}

                else:
                    if user is not None:
                        response = handle_request(user, json_data)
                    else:
                        response = {"status": "error", "message": "User not authenticated"}

                conn.sendall(json.dumps(response).encode("utf-8"))

    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt, exiting")
    finally:
        if conn:
            conn.close()
        if server:
            server.close()
