from server.db.db import DatabaseConnection


class Recommendation:
    def __init__(self):
        self._positive_sentiment = 2
        self._negative_sentiment = -2
        self._neutral_sentiment = 0

    def _calculate_avg_rating(self, food_name: str):
        query = "SELECT AVG(rating) FROM Feedback WHERE food_name = %s"
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (food_name,))
            result = cursor.fetchone()
            return result[0] if result else 0

    def _calculate_avg_sentiment(self, food_name: str):
        query = "SELECT sentiment FROM Feedback WHERE food_name = %s"
        sentiment_scores = {
            "Positive": self._positive_sentiment,
            "Negative": self._negative_sentiment,
            "Neutral": self._neutral_sentiment
        }
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (food_name,))
            sentiments = cursor.fetchall()
            if not sentiments:
                return "Neutral"
            avg_score = sum(sentiment_scores[s[0]] for s in sentiments) / len(sentiments)
            if avg_score > 0:
                return "Positive"
            elif avg_score < 0:
                return "Negative"
            else:
                return "Neutral"

    def _calculate_score(self, food_name: str):
        avg_rating = self._calculate_avg_rating(food_name)
        avg_sentiment = self._calculate_avg_sentiment(food_name)
        sentiment_score = {
            "Positive": self._positive_sentiment,
            "Negative": self._negative_sentiment,
            "Neutral": self._neutral_sentiment
        }
        score = avg_rating + sentiment_score[avg_sentiment]
        return score

    def recommend_food(self, limit=5):
        query = "SELECT food_name FROM Food"
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            food_names = [row[0] for row in cursor.fetchall()]
        
        food_scores = []
        for food_name in food_names:
            score = self._calculate_score(food_name)
            food_scores.append((food_name, score))
        
        food_scores.sort(key=lambda x: x[1], reverse=True)
        top_foods = food_scores[:limit]

        for food_name, score in top_foods:
            avg_rating = self._calculate_avg_rating(food_name)
            avg_sentiment = self._calculate_avg_sentiment(food_name)
            update_query = """
                UPDATE Food
                SET avg_rating = %s, avg_sentiment = %s
                WHERE food_name = %s
            """
            with DatabaseConnection() as conn:
                cursor = conn.cursor()
                cursor.execute(update_query, (avg_rating, avg_sentiment, food_name))
                conn.commit()

        return top_foods
