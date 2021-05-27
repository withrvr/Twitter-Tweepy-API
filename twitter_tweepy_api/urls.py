from django.contrib import admin
from django.urls import path
from Core_App.views import Home_View


urlpatterns = [
    path('admin-panel/', admin.site.urls),

    # Core_App
    path('', Home_View.as_view(), name='Home-Page'),
]
