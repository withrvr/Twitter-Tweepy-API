from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    User_Info_View,
)

app_name = 'Features_App'

urlpatterns = [
    # home page
    path('user-info/', User_Info_View.as_view(), name='User-Info-Page'),

]
