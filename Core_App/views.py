from django.views.generic import TemplateView, RedirectView
from django.urls.base import reverse
from django.shortcuts import render


class Main_Home_View(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # if self.request.user.is_authenticated:
        #     return reverse("Core_App:Home-Page")
        # else:
        #     return reverse("Core_App:Home-Page")

        return reverse("Core_App:Home-Page")


class Home_View(TemplateView):
    template_name = 'Home_Template.html'


class Lorem_Ipsum_View(TemplateView):
    template_name = 'Lorem_Ipsum_Template.html'


def Handle_404_Error_View(request, exception=None, *args, **kwargs):
    return render(request, '404_Error_Template.html')
