import tweepy
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
# TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
# TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
# TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

TWITTER_API_KEY = "ABpINbeG7o19nPmBW3Oms0OEA"
TWITTER_API_SECRET = "37CN0M7KzY5J6TzwQTz7jB7yRtNSbSzQ4WItDilxwkdfe6MKao"
TWITTER_ACCESS_TOKEN = "1584821429446623234-xM6gmLY4ZCzGkF3Frp1EhlzQMor1LG"
TWITTER_ACCESS_SECRET = "amHSPd9FEyGIGtEHscrSyzKq8vduCVDgWLOtroI8Wm6F5"

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
twitter_api = tweepy.API(auth)

def get_twitter_data(query, count=100):
    try:
        tweets = twitter_api.search_tweets(q=query, count=count, tweet_mode="extended")
        return [{"text": tweet.full_text, "likes": tweet.favorite_count, "retweets": tweet.retweet_count} for tweet in tweets]
    except tweepy.errors.Forbidden as e:
        print("Twitter API access is restricted. Skipping Twitter data.")
        return []
    
    
def save_to_csv(data, filename):
    if not data:
        print(f"No data to save for {filename}")
        return
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")
    
twitter_data = get_twitter_data("community engagement")
    
if twitter_data:
    save_to_csv(twitter_data, "twitter_data.csv")