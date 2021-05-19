# Which file does what

## Static Files :

-   [config_tweepy.py](./config_tweepy.py)
    -   connect to twitter api using keys and creatig api object
-   [api_keys.py](./api_keys.py)
    -   content api's keys and tokens variable ( create your own )
    -   ```
        consumer_key = "your_key_value"
        consumer_secret = "your_key_value"
        access_token = "your_key_value"
        access_token_secret = "your_key_value"
        bearer_token = "your_key_value"
        ```

## Dynamic Files ( does some stuff ) :

-   [username_info.py](./username_info.py)
    -   to print the basic information of the user
-   [mentioned_me_with_hashtag.py](./mentioned_me_with_hashtag.py)
    -   to reply to the tweet how have added #withrvr ( can change ) and mentioned you ( my case @withrvr ) in the tweet
-   [search_hashtag_info.py](./search_hashtag_info.py)
    -   make csv file of searched hashtag
    -   can be more than one ( make using and or logic )
