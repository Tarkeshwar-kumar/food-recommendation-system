from server.db.db import DatabaseConnection, DatabaseMethods


class Recommendation:
    def __init__(self):
        self._positive_sentiment = 2
        self._negative_sentiment = -2
        self._neutral_sentiment = 0
        self.sentiment_scores = {
            "Positive": self._positive_sentiment,
            "Negative": self._negative_sentiment,
            "Neutral": self._neutral_sentiment
        }

    def _calculate_avg_rating(self, food_name: str):
        db = DatabaseMethods()
        return db.calculate_avg_rating(food_name)

    def _calculate_avg_sentiment(self, food_name: str):
        db = DatabaseMethods()
        
        return db.get_sentiment(food_name, self.sentiment_scores)

    def _calculate_score(self, food_name: str):
        avg_rating = self._calculate_avg_rating(food_name)
        avg_sentiment = self._calculate_avg_sentiment(food_name)

        if avg_rating == None:
            avg_rating = 0
        score = avg_rating + self.sentiment_scores[avg_sentiment]
        return score

    def recommend_food(self, user_id, limit=5):
        db = DatabaseMethods()
        user_preferences = db.get_user_preferences(user_id)
        food_names = db.get_food_list_for_user(user_preferences)
        
        food_scores = []
        for food in food_names:
            for food_name in food:
                score = self._calculate_score(food_name)
                food_scores.append((food_name, score))
        
        food_scores.sort(key=lambda x: x[1], reverse=True)
        top_foods = food_scores[:min(limit, len(food_scores))]
        

        return top_foods
