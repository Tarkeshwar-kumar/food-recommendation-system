from dataclasses import dataclass
from src.server.model.feedback import Feedback


@dataclass
class Food:

    food_name: str
    price: int
    availability_status: bool
    category: str
    avg_rating: float
    feedbacks: list[Feedback]

    def calculate_avg_rating():
        pass

    def get_avg_rating():
        pass