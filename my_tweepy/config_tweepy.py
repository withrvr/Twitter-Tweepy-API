# comman config code is in this file
# for twitter api connection to key and creatig api object

import tweepy
from . import api_keys

# change your api_keys in api_keys.py
# taking my keys form the py file
# so that i can change at any time
# and its known to me only
consumer_key = api_keys.consumer_key
consumer_secret = api_keys.consumer_secret
access_token = api_keys.access_token
access_token_secret = api_keys.access_token_secret

# create authentication for accessing Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialize Tweepy API
# api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
