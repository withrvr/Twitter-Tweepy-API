from django.views.generic import TemplateView
from my_tweepy.config_tweepy import api, tweepy
import json
import requests


# ---------------------------- user-most-popular ------------------------------------------
class User_Most_Popular_Choice_View(TemplateView):
    template_name = 'Features_App/User_Most_Popular/Choice_Template.html'


class User_Most_Popular_Followers_View(TemplateView):
    template_name = 'Features_App/User_Most_Popular/Followers_Template.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # getting username
        user = self.request.GET.get('user', None)

        if user in (None, ""):
            context["status"] = 'not_enter'
        else:
            context["status"] = 'enter'
            try:
                followers_response = tweepy.Cursor(api.followers, user).items()

                screen_name = []
                followers_count = []

                for follower in followers_response:
                    screen_name.append(follower.screen_name)
                    followers_count.append(follower.followers_count)

                context["screen_name_json"] = json.dumps(screen_name)
                context["followers_count_json"] = json.dumps(followers_count)

                followers = list(zip(followers_count, screen_name))
                sorted_followers = sorted(
                    followers, key=lambda follower: (
                        follower[0], follower[1]
                    ),
                    reverse=True
                )
                print(sorted_followers)
                context["followers"] = sorted_followers

            except Exception as error:
                context["status"] = 'error'
                context["error"] = error

        return context


class User_Most_Popular_Following_View(TemplateView):
    template_name = 'Features_App/User_Most_Popular/Following_Template.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # getting username
        user = self.request.GET.get('user', None)

        if user in (None, ""):
            context["status"] = 'not_enter'
        else:
            context["status"] = 'enter'
            try:
                following_response = tweepy.Cursor(api.friends, user).items()

                screen_name = []
                followers_count = []

                for follow in following_response:
                    screen_name.append(follow.screen_name)
                    followers_count.append(follow.followers_count)

                context["screen_name_json"] = json.dumps(screen_name)
                context["followers_count_json"] = json.dumps(followers_count)

                following = list(zip(followers_count, screen_name))
                sorted_following = sorted(
                    following, key=lambda follow: (
                        follow[0], follow[1]
                    ),
                    reverse=True
                )
                print(sorted_following)
                context["following"] = sorted_following

            except Exception as error:
                context["status"] = 'error'
                context["error"] = error

        return context


# ---------------------------- Compare_View ------------------------------------------
def parse_as_tags_array(somestring):
    # remove spaces and split with ','
    somestring = somestring.replace(" ", "").split(",")
    # remove black string if content in the array.. ex ['', '', ]
    somearray = ' '.join(somestring).split()
    # remove dupicate values
    somearray = list(set(somearray))
    return somearray


class Compare_Choice_View(TemplateView):
    template_name = 'Features_App/Compare/Choice_Template.html'


class Compare_Tweets_View(TemplateView):
    template_name = 'Features_App/Compare/Tweets_Template.html'

    def find_tweets_likes(self, tweets):
        tweets = parse_as_tags_array(tweets)

        tweets_found = []
        tweets_notfound = []
        tweets_likes = []

        for tweet in tweets:
            try:
                tweet_responce = api.get_status(tweet)._json
                tweets_found.append(
                    f'{tweet_responce["user"]["screen_name"]} - {tweet_responce["id"]}'
                )
                tweets_likes.append(tweet_responce["favorite_count"])
            except:
                tweets_notfound.append(tweet)

        return tweets_found, tweets_notfound, tweets_likes

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        tweets = self.request.GET.get('tweets', None)

        if tweets in (None, ""):
            context["status"] = 'not_enter'
        else:
            context["status"] = 'enter'
            try:
                tweets_found, tweets_notfound, tweets_likes = self.find_tweets_likes(
                    tweets
                )

                context["tweets_found"] = json.dumps(tweets_found)
                context["tweets_notfound"] = json.dumps(tweets_notfound)
                context["tweets_followers"] = json.dumps(tweets_likes)

            except Exception as error:
                print(error)
                context["status"] = 'error'
                context["error"] = error

        return context


class Compare_Users_View(TemplateView):
    template_name = 'Features_App/Compare/Users_Template.html'

    def find_users_followers(self, users):
        users = parse_as_tags_array(users)

        users_found = []
        users_notfound = []
        users_followers = []

        for user in users:
            try:
                user_responce = api.get_user(user)._json
                users_found.append(user_responce["screen_name"])
                users_followers.append(user_responce["followers_count"])
            except:
                users_notfound.append(user)

        return users_found, users_notfound, users_followers

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        users = self.request.GET.get('users', None)

        if users in (None, ""):
            context["status"] = 'not_enter'
        else:
            context["status"] = 'enter'
            try:

                users_found, users_notfound, users_followers = self.find_users_followers(
                    users
                )

                context["users_found"] = json.dumps(users_found)
                context["users_notfound"] = json.dumps(users_notfound)
                context["users_followers"] = json.dumps(users_followers)

            except Exception as error:
                print(error)
                context["status"] = 'error'
                context["error"] = error

        return context


class Search_View(TemplateView):
    template_name = 'Features_App/Search_Template.html'

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

        if username in (None, ""):
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
