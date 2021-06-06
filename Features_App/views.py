from django import template
from django.views.generic import TemplateView
from my_tweepy.config_tweepy import api, tweepy
import json
import requests
# import copy


class Contents_Hashtag_View(TemplateView):
    template_name = 'Features_App/Contents_Hashtag_Template.html'

    def get_tweets_html(self, url, *args, **kwargs):
        twtjson = requests.get(
            'https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
        twtparse = twtjson.json()
        twthtml = twtparse['html']
        return twthtml

    def csv_data(self, tweets):

        import pandas as pd
        rows = [
            [
                tweet.created_at,
                tweet.id,
                tweet.full_text,
                tweet.retweet_count,
                tweet.favorite_count,
                ",".join([hashtag["text"]
                          for hashtag in tweet.entities["hashtags"]]),
                tweet.user.id,
                tweet.user.name,
                tweet.user.screen_name,
                tweet.user.followers_count,
                tweet.user.friends_count,
                tweet.user.verified,
                tweet.user.statuses_count,
            ]
            for tweet in tweets
        ]

        cols = [
            "created_at",
            "id",
            "text",
            "retweet_count",
            "likes",

            "hashtags",

            "user_id",
            "user_name",
            "user_screen_name",
            "user_followers_count",
            "user_friends_count",
            "user_verified",
            "user_no_of_tweets",
        ]

        csv_df = pd.DataFrame(rows, columns=cols)
        csv_data = csv_df.to_csv()
        return csv_data

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search = self.request.GET.get('search', None)
        items = self.request.GET.get('items', None)

        if search in (None, "") or items in (None, ""):
            context["status"] = 'not_enter'
        else:
            context["status"] = 'enter'
            try:
                tweets = tweepy.Cursor(
                    api.search, q=search, lang="en", tweet_mode='extended'
                ).items(int(items))

                tweets = list(tweets)

                tweets_json = [json.dumps(tweet._json, indent=4)
                               for tweet in tweets]

                context["data"] = zip(tweets, tweets_json)

                context["csv_data"] = self.csv_data(tweets)

            except tweepy.TweepError as error:
                context["status"] = 'error'
                context["error"] = error
            except (ValueError, TypeError) as error:
                context["status"] = 'error'
                context["error"] = 'Enter Values Properly'
            except Exception as error:
                print(error)
                context["status"] = 'error'
                context["error"] = error

        return context


class User_Info_View(TemplateView):
    template_name = 'Features_App/User_Info_Template.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # getting username
        username = self.request.GET.get('username', None)

        if username == None or username == "":
            context["user_status"] = 'user_not_enter'
        else:
            context["user_status"] = 'user_enter'
            try:
                response = api.get_user(username)
                json_responce = response._json
                context["user"] = json_responce
                context["user_json"] = json.dumps(json_responce, indent=4)
            except tweepy.TweepError as error:
                context["user_status"] = 'user_not_found'
                context["user_error"] = error

        return context
