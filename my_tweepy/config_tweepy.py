# comman config code is in this file
# for twitter api connection to key and creatig api object

import tweepy
import os
# change your api_keys in api_keys.py
# taking my keys form the py file
# so that i can change at any time
# and its known to me only
CONSUMER_KEY = os.environ.get('TTI_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TTI_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TTI_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TTI_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.environ.get('TTI_BEARER_TOKEN')

# create authentication for accessing Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# initialize Tweepy API
# api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
