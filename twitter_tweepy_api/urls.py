from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin-panel/', admin.site.urls),

    # Core_App
    path('', include('Core_App.urls')),

]
