import urllib, json, os
from urllib import request
from django import template

register = template.Library()

@register.filter(name='loadjson')
def loadjson(value):
    url = "https://graph.instagram.com/me/media?fields=caption,id,media_type,media_url&access_token="+os.environ.get('INSTAGRAM_DEV_TOKEN')
    json_url = urllib.request.urlopen(url)
    json_object = json.loads(json_url.read())
    json_valuable = json_object["data"]
    return json_valuable
    
@register.filter(is_safe=True)
def myfilter(value):
    return value