
import random


def predict_sentiment(text: str):
    """
    predict whether text is positive or negative
    """

    return random.sample(["positive", "negative"], 1)[0]


# TRUE WHEN SELF RUN , FALSE WHEN IMPORT RUN
if __name__ == "__main__": 
    prediction = predict_sentiment("i am hungry!")
    print(prediction)
