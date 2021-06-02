from django.views.generic import TemplateView
from my_tweepy.config_tweepy import api, tweepy
import json


class User_Info_View(TemplateView):
    template_name = 'Features_App/User_Info_Template.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        not_enter = 'user_not_enter'

        # getting username
        username = self.request.GET.get('username', not_enter)

        if username == not_enter:
            context["user_status"] = not_enter
        else:
            context["user_status"] = 'user_enter'
            try:
                response = api.get_user(username)
                json_responce = response._json
                context["user"] = json_responce
            except tweepy.TweepError as e:
                context["user_status"] = 'user_not_found'

        return context
