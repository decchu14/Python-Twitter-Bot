import tweepy
import time
import MyAPIKeys  # just created a seperate python file to keep my keys so that i can just import it instead of typing it again and again

# setting auth
auth = tweepy.OAuthHandler(MyAPIKeys.Api_Key, MyAPIKeys.Api_Key_Secret)
auth.set_access_token(MyAPIKeys.Access_Token, MyAPIKeys.Access_Token_Secret)

api = tweepy.API(auth)
user = api.me()


# there is a limit of 200 to hit twitter api as soon as the limit met the twitter api is going to raise an limit error.
# so this function is to handle that error and pause for some time and then continue
# so that this script doesnt break the rule

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# here count is 200 means 200 times we can hit the api and fetch 200 tweets each at a time
# just to not get confused, screen name is which begins with @, excluding @.
all_tweets = api.user_timeline(screen_name="[screenname]", count=200)
# just a counter to count tweets
count1 = 0
# if you want to fetch more than 200 tweets than replace the below for loop with
# for tweet in limit_handler(all_tweets): so that it can handle limit error
for tweet in all_tweets:
    try:
        if not tweet.favorited:
            count1 += 1
            print("\n")
            # print(count1) if you want to print the count also
            tweet.favorite()
            print(tweet.text.encode('utf8'))  # to print the tweets
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

print(f'you favorited {count1} tweets')
