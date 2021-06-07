from django.urls import path

from .views import (
    User_Info_View,
    Search_View,
    Compare_Users_View,
    Compare_Tweets_View,
)

app_name = 'Features_App'

urlpatterns = [
    path('user-info/', User_Info_View.as_view(), name='User-Info-Page'),
    path('search/',
         Search_View.as_view(), name='Search-Page'),
    path('compare-users/', Compare_Users_View.as_view(), name='Compare-Users-Page'),
    path('compare-Tweets/', Compare_Tweets_View.as_view(),
         name='Compare-Tweets-Page'),

]
