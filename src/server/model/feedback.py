from dataclasses import dataclass


@dataclass
class Feedback:

    food_name: str
    comments: str
    rating: float
    is_liked: bool
    user_id: str
    sentiment: str