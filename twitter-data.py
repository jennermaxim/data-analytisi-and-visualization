import tweepy
import csv

TWITTER_API_KEY = "TWITTER_API_KEY"  # Replace with your actual API key
TWITTER_API_SECRET = "TWITTER_API_SECRET"  # Replace with your actual API secret
TWITTER_ACCESS_TOKEN = "TWITTER_ACCESS_TOKEN"  # Replace with your actual access token
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"  # Replace with your actual access secret

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