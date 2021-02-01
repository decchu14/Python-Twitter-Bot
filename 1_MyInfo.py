import tweepy
import MyAPIKeys  # just created a seperate python file to keep my keys so that i can just import it instead of typing it again and again


auth = tweepy.OAuthHandler(MyAPIKeys.Api_Key, MyAPIKeys.Api_Key_Secret)
auth.set_access_token(MyAPIKeys.Access_Token, MyAPIKeys.Access_Token_Secret)

api = tweepy.API(auth)


user = api.me()
print(user.name)  # fetching twitter user name

print(user.screen_name)  # fetching twitter screen name
print(user.followers_count)  # fetching the count of followers

# this block fetches the tweets from the homeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
