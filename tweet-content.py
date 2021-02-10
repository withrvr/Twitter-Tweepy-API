"""
this py code
reply to the tweet which content #withrvr and @withrvr in the tweet
"""

import tweepy
import api_keys

try:
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
    api = tweepy.API(auth)

    # taking out the tweets who have mention me
    mentions = api.mentions_timeline()
    hashtag_should_content = '#withrvr'

    # looping over tweets how have mention me
    for mention in reversed(mentions):
        if hashtag_should_content in mention.text.lower():
            user_name = mention.user.screen_name

            print(mention.id, "-", mention.user.screen_name, "-", mention.text)

            msg = "..@" + user_name + " thanks to mention me and using hashtag #withrvr"
            api.update_status(msg, mention.id)


except Exception as e:
    print(e)
