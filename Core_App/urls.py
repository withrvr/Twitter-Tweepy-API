from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    # core
    Home_View,
    Main_Home_View,

    # lorem
    Lorem_Ipsum_View,

    # errors
    Handle_404_Error_View,
)

app_name = 'Core_App'

urlpatterns = [
    # home page
    path('', Main_Home_View.as_view(), name='Main-Home-Page'),
    path('home/', Home_View.as_view(), name='Home-Page'),

    # erros
    path('404/', Handle_404_Error_View, name='404-Page'),


    # lorem ipsum
    path('lorem/', Lorem_Ipsum_View.as_view(), name='Lorem-Ipsum-Page'),
    path('ipsum/', Lorem_Ipsum_View.as_view()),
    path('loremipsum/', Lorem_Ipsum_View.as_view()),
    path('lorem-ipsum/', Lorem_Ipsum_View.as_view()),
]
