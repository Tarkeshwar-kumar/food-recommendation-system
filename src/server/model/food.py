from dataclasses import dataclass
from server.model.feedback import Feedback


@dataclass
class Food:

    food_name: str
    price: int
    availability_status: bool
    category: str
    avg_rating: float
    feedbacks: list[Feedback]
    food_type: str

    def calculate_avg_rating():
        pass

    def get_avg_rating():
        pass

    def create_food_item(json_data):

        print(json_data)
