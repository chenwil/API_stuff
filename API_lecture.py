import requests
import secrets


def get_stories(section):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/"
    extended_url = baseurl + section + '.json'
    params = {'api-key' : secrets.nyt_key}
    return requests.get(extended_url, params).json()


section = 'science'
stories = get_stories(section)
print(stories)
