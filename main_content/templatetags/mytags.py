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
    
@register.filter(name='countpianos4divelement')
def countpianos4divelement(pianos):
    count = 0
    for piano in pianos:
        count += 1
    if (count % 4 == 0):
        return ''
    else:    
        return '</div>'

@register.filter(name='countpianos2divelement')
def countpianos2divelement(pianos):
    count = 0
    for piano in pianos:
        count += 1
    if (count % 2 == 0):
        return ''
    else:    
        return '</div>'