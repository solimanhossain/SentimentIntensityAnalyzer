# pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getSIA(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

string = input("Sentence : ")

SIA = getSIA(string)
print(f"Positive: {SIA['pos']}\tNegative: {SIA['neg']}\tNeutral: {SIA['neu']}\tCompound: {SIA['compound']}")