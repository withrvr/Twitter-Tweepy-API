from django.urls import path

from .views import (
    User_Info_View,
    Search_View,

    # compare
    Compare_Choice_View,
    Compare_Users_View,
    Compare_Tweets_View,

    # user-most-popular
    User_Most_Popular_Choice_View,
    User_Most_Popular_Followers_View,
    User_Most_Popular_Following_View,
)

app_name = 'Features_App'

urlpatterns = [
    path('user-info/', User_Info_View.as_view(), name='User-Info-Page'),
    path(
        'search/',
        Search_View.as_view(),
        name='Search-Page'
    ),

    # compare
    path('compare/', Compare_Choice_View.as_view(), name='Compare-Choice-Page'),
    path('compare/users/', Compare_Users_View.as_view(), name='Compare-Users-Page'),
    path(
        'compare/tweets/',
        Compare_Tweets_View.as_view(),
        name='Compare-Tweets-Page'
    ),

    # user-most-popular
    path(
        'user-most-popular/',
        User_Most_Popular_Choice_View.as_view(),
        name='User-Most-Popular-Choice-Page'
    ),
    path(
        'user-most-popular/followers/',
        User_Most_Popular_Followers_View.as_view(),
        name='User-Most-Popular-Followers-Page'
    ),
    path(
        'user-most-popular/following/',
        User_Most_Popular_Following_View.as_view(),
        name='User-Most-Popular-Following-Page'
    ),

]
