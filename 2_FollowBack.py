import tweepy
import time
import MyAPIKeys  # just created a seperate python file to keep my keys so that i can just import it instead of typing it again and again

# setting the auth
auth = tweepy.OAuthHandler(MyAPIKeys.Api_Key, MyAPIKeys.Api_Key_Secret)
auth.set_access_token(MyAPIKeys.Access_Token, MyAPIKeys.Access_Token_Secret)

api = tweepy.API(auth)

user = api.me()

# there is a limit to hit twitter api as soon as the limit met the twitter api is going to raise an limit error.
# so this function is to handle that error and pause for some time and then continue
# so that this script doesnt break the rule


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        pass


# cursor allows us to navigate through all the pages in twiiter to fetch necessary information
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()
    print("followed ", follower.screen_name)
