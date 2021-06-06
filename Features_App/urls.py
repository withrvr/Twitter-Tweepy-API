from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    User_Info_View,
    Contents_Hashtag_View
)

app_name = 'Features_App'

urlpatterns = [
    path('user-info/', User_Info_View.as_view(), name='User-Info-Page'),
    path('contents-hashtag/',
         Contents_Hashtag_View.as_view(), name='Contents-Hashtag-Page'),
]
