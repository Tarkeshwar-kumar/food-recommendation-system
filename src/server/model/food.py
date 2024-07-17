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
    spice_level: str
    is_sweet: int
    region: str
