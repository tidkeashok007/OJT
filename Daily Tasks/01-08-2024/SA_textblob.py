#textblob library
from textblob import TextBlob
#create a sample text

texts =[
     "I love NLP ! It's works great and I'm very satisfied",
     "This my first experince on doing sentiment analysis , I am littale bit disappointed",
     "The NLP sentiment analysis is quiet intreseting it is neither good or bad",
]

#create function to do the sentiment analysis
def analyze_sentiment(text):
     analysis = TextBlob(text)
     #-1.0 - 1.0 polarity score
     polarity = analysis.sentiment.polarity
     if polarity>0:
          sentiment = "Positive"
     elif polarity<0:
          sentiment = "Negative"
     else:
          sentiment = "neutral"
     return sentiment

for text in texts:
     sentiment = analyze_sentiment(text)
     print(f"Text:{text}")
     print(f"Sentiment:{sentiment}")