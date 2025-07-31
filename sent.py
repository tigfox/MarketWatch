import tweepy
import json

# Replace with your own Bearer Token
BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'

# Create a Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Replace with the username you want tweets from (without @)
username = "elonmusk"

# Get user ID
user = client.get_user(username=username)
user_id = user.data.id

# Fetch recent tweets
tweets = client.get_users_tweets(
    id=user_id,
    max_results=10,  # max is 100 per request
    tweet_fields=['created_at', 'text']
)

# Extract and format as JSON
tweet_list = [{"id": tweet.id, "created_at": str(tweet.created_at), "text": tweet.text} for tweet in tweets.data]

# Output JSON
with open("tweets.json", "w") as f:
    json.dump(tweet_list, f, indent=2)

print(json.dumps(tweet_list, indent=2))
