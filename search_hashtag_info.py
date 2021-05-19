
from config_tweepy import api, tweepy

# import json
import csv
# import re

try:

    # hashtag_phrase = input('Hashtag Phrase :- ')
    hashtag_phrase = '#java or #python'  # hashtag_phrase = '#java and #python'

    # get the name of the spreadsheet we will write to
    # fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))
    fname = 'foo'  # .... ie. foo.csv

    # open the spreadsheet we will write to
    with open(f'{fname}.csv', 'wb') as file:

        w = csv.writer(file)

        # write header row to spreadsheet
        w.writerow([
            'timestamp', 'tweet_text', 'username', 'followers_count', 'all_hashtags',
        ])

        # for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(
            api.search,
            q=hashtag_phrase+' -filter:retweets',
            lang="en",
            tweet_mode='extended'
        ).items(5):
            # loop stated
            w.writerow(
                [tweet.created_at,
                 tweet.full_text.replace('\n', ' ').encode('utf-8'),
                 tweet.user.screen_name.encode('utf-8'),
                 tweet.user.followers_count,
                 [e['text'] for e in tweet._json['entities']['hashtags']],
                 ]
            )


except Exception as e:
    from error_msg import exception_error
    exception_error(e)
