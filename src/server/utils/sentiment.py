import re
from abc import ABC, abstractmethod

# Define keywords with weights for positive, negative, and neutral sentiments
positive_keywords = {"delicious": 3, "tasty": 2, "excellent": 3, "amazing": 3, "great": 2, "perfect": 3, "fantastic": 3, "fresh": 2, "flavorful": 2}
negative_keywords = {"terrible": 3, "awful": 2, "bad": 1, "horrible": 3, "disgusting": 3, "stale": 2, "bland": 2, "overcooked": 2, "undercooked": 2}
neutral_keywords = {"average": 0, "okay": 0, "fine": 0, "decent": 0, "mediocre": 0}

# Compile regex patterns for positive, negative, and neutral keywords
positive_pattern = re.compile('|'.join(positive_keywords.keys()), re.IGNORECASE)
negative_pattern = re.compile('|'.join(negative_keywords.keys()), re.IGNORECASE)
neutral_pattern = re.compile('|'.join(neutral_keywords.keys()), re.IGNORECASE)

# Define the abstract base class
class Sentiment(ABC):
    @abstractmethod
    def get_sentiment(self, text):
        pass

# Define the RuleBasedSentiment class that inherits from Sentiment
class RuleBasedSentiment(Sentiment):
    def get_sentiment(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
            
        # Find all occurrences of positive, negative, and neutral keywords
        positive_matches = positive_pattern.findall(text)
        negative_matches = negative_pattern.findall(text)
        neutral_matches = neutral_pattern.findall(text)

        # Calculate the polarity score based on keyword weights
        polarity_score = sum(positive_keywords[word.lower()] for word in positive_matches)
        polarity_score -= sum(negative_keywords[word.lower()] for word in negative_matches)

        # Determine sentiment based on the polarity score
        if polarity_score > 1:
            sentiment = "Positive"
        elif polarity_score < -1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            strength = "None"

        return {"Sentiment": sentiment}


text1 = "The pizza was delicious and perfectly cooked."
text2 = "The steak was overcooked and tasted terrible."
text3 = "The salad was okay, not bad but not great either."

sentiment_analyzer = RuleBasedSentiment()

try:
    sentiment1 = sentiment_analyzer.get_sentiment(text1)
    sentiment2 = sentiment_analyzer.get_sentiment(text2)
    sentiment3 = sentiment_analyzer.get_sentiment(text3)

    print("Sentiment of text1:", sentiment1)
    print("Sentiment of text2:", sentiment2)
    print("Sentiment of text3:", sentiment3)
except ValueError as e:
    print(e)
