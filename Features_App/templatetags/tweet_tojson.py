from django import template
import json

register = template.Library()


@register.simple_tag
def tweet_tojson(tweet):
    tweet_json = json.dumps(tweet._json, indent=4)
    return tweet_json
