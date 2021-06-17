# Which file does what

## Static Files :

-   [config_tweepy.py](./my_tweepy/config_tweepy.py)
    -   connect to twitter api using keys and creatig api object
-   [Set this as environment variables](./.env_file)
    

## Dynamic Files ( does some stuff ) :

-   [username_info.py](./my_tweepy/username_info.py)
    -   to print the basic information of the user
-   [mentioned_me_with_hashtag.py](./my_tweepy/mentioned_me_with_hashtag.py)
    -   to reply to the tweet how have added #withrvr ( can change ) and mentioned you ( my case @withrvr ) in the tweet
-   [search_hashtag_info.py](./my_tweepy/search_hashtag_info.py)
    -   make csv file of searched hashtag
    -   can be more than one ( make using and or logic )
