from .config_tweepy import api, tweepy

try:
    print()
    user_name = input("Enter UserName Like (withrvr):- ")
    print()
    user = api.get_user(user_name)

    # uncoment below code to save the user data in foo.json file
    # import json
    # with open('foo.json', 'w') as file:
    #     json.dump(user._json, file, indent=4)

    print()
    print("Name                   :- ", user.name)
    print("Username               :- ", user.screen_name)
    print("Followers Count        :- ", user.followers_count)
    print("Following Count        :- ", user.friends_count)
    print()
    print("URL (link) of Website  :- ", user.url)
    print("location/ Lives        :- ", user.location)
    print("Verified ( Blue Tick ) :- ", user.verified)
    print("Account Created At     :- ", user.created_at)
    print()
    print("Description            :- ", user.description)
    print()

except tweepy.TweepError as e:

    print(f"\n{user} :- {e.args[0][0]['message']}\n")

except Exception as e:

    from .error_msg import exception_error
    exception_error(e)

finally:
    pass
