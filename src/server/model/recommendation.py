from server.db.db import DatabaseConnection, DatabaseMethods


class Recommendation:
    def __init__(self):
        self._positive_sentiment = 2
        self._negative_sentiment = -2
        self._neutral_sentiment = 0

    def _calculate_avg_rating(self, food_name: str):
        db = DatabaseMethods()
        return db.calculate_avg_rating(food_name)

    def _calculate_avg_sentiment(self, food_name: str):
        db = DatabaseMethods()
        sentiment_scores = {
            "Positive": self._positive_sentiment,
            "Negative": self._negative_sentiment,
            "Neutral": self._neutral_sentiment
        }
        return db.get_sentiment(food_name, sentiment_scores)

    def _calculate_score(self, food_name: str):
        avg_rating = self._calculate_avg_rating(food_name)
        avg_sentiment = self._calculate_avg_sentiment(food_name)
        sentiment_score = {
            "Positive": self._positive_sentiment,
            "Negative": self._negative_sentiment,
            "Neutral": self._neutral_sentiment
        }
        if avg_rating == None:
            avg_rating = 0
        score = avg_rating + sentiment_score[avg_sentiment]
        return score

    def recommend_food(self, limit=5):
        db = DatabaseMethods()
        food_names = db.get_food_list()
        
        food_scores = []
        for food_name in food_names:
            score = self._calculate_score(food_name)
            # print(score)
            food_scores.append((food_name, score))
        
        food_scores.sort(key=lambda x: x[1], reverse=True)
        top_foods = food_scores[:]

        for food_name, score in top_foods:
            avg_rating = self._calculate_avg_rating(food_name)
            if avg_rating == None:
                avg_rating = 0
            avg_sentiment = self._calculate_avg_sentiment(food_name)
            update_query = """
                UPDATE Food
                SET avg_rating = %s, avg_sentiment = %s
                WHERE food_name = %s
            """
            db.update_food_ratings(update_query, avg_rating, avg_sentiment, food_name)

        return top_foods
