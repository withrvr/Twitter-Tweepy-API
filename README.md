# Twitter-API ... repo ???

Twitter-API using python to do diffrent stuff

<br/>

# Sites ( Links )

-   [Twitter - @withrvr Account](https://twitter.com/withrvr)
    <br><br>
-   [Tweepy Module Docs](https://docs.tweepy.org/)
-   [Twitter API Docs](https://developer.twitter.com/en/docs/twitter-api)

<br>

# How to execute ( or Steps to Follow)

-   Fork and pull - OR - download this repo
-   Download python
-   `pip install tweepy` ( Download tweepy module )
-   Create File -- api_key.py -- add this code with there api keys value -- [click to know the location](Twitter-API-Python-Code/)

```
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
```

-   Now run :- `python File_Name.py`

<br>

# Which file does what

## <u>Static Files:-</u>

-   [config_tweepy.py](Twitter-API-Python-Code/config_tweepy.py)
    -   connect to twitter api using keys and creatig api object
-   [api_keys.py](Twitter-API-Python-Code/api_keys.py)
    -   content api's keys and tokens variable with values

## <u>Dynamic Files ( means run this file for corresponding results ):-</u>

-   [username_info.py](Twitter-API-Python-Code/username_info.py)
    -   to print the basic information of the user
-   [mentioned_me_with_hashtag.py](Twitter-API-Python-Code/mentioned_me_with_hashtag.py)
    -   to reply to the tweet how have added #withrvr ( can change ) and mentioned you ( my case @withrvr ) in the tweet
-   [search_hashtag_info.py](Twitter-API-Python-Code/search_hashtag_info.py)
    -   make csv file of searched hashtag
    -   can be more than one ( make using and or logic )
