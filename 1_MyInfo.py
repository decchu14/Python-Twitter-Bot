import tweepy
import MyAPIKeys  # just created a seperate python file to keep my keys so that i can just import it instead of typing it again and again

# setting the auth
auth = tweepy.OAuthHandler(MyAPIKeys.Api_Key, MyAPIKeys.Api_Key_Secret)
auth.set_access_token(MyAPIKeys.Access_Token, MyAPIKeys.Access_Token_Secret)
api = tweepy.API(auth)


user = api.me()
print(user.name)  # fetching my twitter user name

print(user.screen_name)  # fetching my twitter screen name
print(user.followers_count)  # fetching my count of followers

# this block fetches the tweets from the my homeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    tweet = tweet.text.encode('utf8')
    print(tweet, "\n")
