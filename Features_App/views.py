from django.views.generic import TemplateView
from my_tweepy.config_tweepy import api, tweepy
import json


class User_Info_View(TemplateView):
    template_name = 'Features_App/User_Info_Template.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # getting username
        username = self.request.GET.get('username', None)

        if username == None or username == "":
            context["user_status"] = 'user_not_enter'
        else:
            context["user_status"] = 'user_enter'
            try:
                response = api.get_user(username)
                json_responce = response._json
                context["user"] = json_responce
                context["user_json"] = json.dumps(json_responce, indent=4)
            except tweepy.TweepError as error:
                context["user_status"] = 'user_not_found'
                context["user_error"] = error
                print()
                print(error)
                print()

        return context
