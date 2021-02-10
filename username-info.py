
# this is the funciton which content the main code
# or the code which perform the main operation

def main_code():

    try:
        print()
        user_name = input("Enter UserName Like (withrvr):- ")
        print()
        user = api.get_user(user_name)

        # it save the user data in json file name 'foo.txt'
        # with open('foo.json', 'w') as file:
        #     json.dump(user._json, file, indent=4)

        print()
        print("Name                   :- ", user.name)
        print("Username               :- ", user.screen_name)
        print("Followers Count        :- ", user.followers_count)
        print("Following Count        :- ", user.friends_count)
        print()
        print("URL / Website / Link   :- ", user.url)
        print("location/ Lives        :- ", user.location)
        print("Verified ( Blue Tick ) :- ", user.verified)
        print("Account Created At     :- ", user.created_at)
        print()
        print("Description            :- ", user.description)
        print()
    except tweepy.error.TweepError as e:
        enter_key()

    except Exception as e:
        print(e)
        print("\n- - - - - Error - - - - -")
        print("Enter Correct Username")
        print("There is not User with username :-  ''", user_name, "''")
        print("- - - - - Error - - - - -\n")
        main_code()


# functions that prints the error if its there
def enter_key():
    print("\n\nEnter this data proper")
    print("consumer_key, consumer_secret, access_token, access_token_secret")
    print("\nyour keys value should be correct and not blank also")
    print("\n\n")


# -------------------------------------------
# this is accutor starting of the code
# before is actually the def ( functions )
# -------------------------------------------
try:
    import tweepy
    import api_keys

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

    # ..................... starting of the main code is from here ................

    main_code()

except tweepy.error.TweepError as e:
    enter_key()

except Exception as e:
    print("Soem Error is there:-- \n\n", e)
