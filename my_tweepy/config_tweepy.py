# comman config code is in this file
# for twitter api connection to key and creatig api object

import tweepy
from decouple import config

# change your api_keys in api_keys.py
# taking my keys form the py file
# so that i can change at any time
# and its known to me only
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = config('BEARER_TOKEN')

# create authentication for accessing Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# initialize Tweepy API
# api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
