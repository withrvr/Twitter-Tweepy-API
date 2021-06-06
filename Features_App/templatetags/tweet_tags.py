import requests
from django import template


register = template.Library()


@register.simple_tag
def tweet_tags(screen_name, id):
    """ Requests a tweet from oembed and returns the html element """

    url = f"https://twitter.com/{screen_name}/status/{id}"

    tweet_request = requests.get(
        'https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
    tweet_json = tweet_request.json()
    tweet_html = tweet_json['html']

    return tweet_html
