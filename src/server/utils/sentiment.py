import re
from abc import ABC, abstractmethod

positive_keywords = {
    "delicious": 3, "tasty": 2, "excellent": 3, "amazing": 3, "great": 2,
    "perfect": 3, "fantastic": 3, "fresh": 2, "flavorful": 2, "good": 2,
    "superb": 3, "wonderful": 3, "awesome": 3, "yummy": 2, "pleasing": 2,
    "satisfying": 2, "divine": 3, "scrumptious": 3, "heavenly": 3
}

negative_keywords = {
    "terrible": 3, "awful": 2, "bad": 1, "horrible": 3, "disgusting": 3,
    "stale": 2, "bland": 2, "overcooked": 2, "undercooked": 2, "poor": 1,
    "mediocre": 1, "disappointing": 2, "gross": 2, "unsatisfactory": 2,
    "tasteless": 2, "inedible": 3, "revolting": 3, "nasty": 2, "repulsive": 3
}

positive_pattern = re.compile('|'.join(positive_keywords.keys()), re.IGNORECASE)
negative_pattern = re.compile('|'.join(negative_keywords.keys()), re.IGNORECASE)

class Sentiment(ABC):
    @abstractmethod
    def get_sentiment(self, text):
        pass

class RuleBasedSentiment(Sentiment):
    def get_sentiment(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
            
        positive_matches = positive_pattern.findall(text)
        negative_matches = negative_pattern.findall(text)

        polarity_score = sum(positive_keywords[word.lower()] for word in positive_matches)
        polarity_score -= sum(negative_keywords[word.lower()] for word in negative_matches)

        if polarity_score > 1:
            sentiment = "Positive"
        elif polarity_score < -1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {"Sentiment": sentiment}