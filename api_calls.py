import requests
import os
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
bearer_token=os.environ["BEARER_TOKEN"]
    
spoonacular_key=os.environ['SPOON_KEY']

def auth():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)

# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def create_twitter_url(rand_food):
    query = rand_food
    tweet_fields = "created_at,lang"
    user_fields = "username,name"
    url = "https://api.twitter.com/2/tweets/search/recent?expansions=author_id&query={}&tweet.fields={}&user.fields={}".format(
        query, tweet_fields, user_fields
    )
    return url
    
    
def create_spoon_url(rand_food):
    query = rand_food
    fields = ""
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}&query={}".format(spoonacular_key, query)
    return url

def getRecipeInfo(recipe_id):
    url = "https://api.spoonacular.com/recipes/{}/information?apiKey={}".format(recipe_id, spoonacular_key)
    headers = {}
    response = connect_to_spoon_endpoint(url)
    return response


# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def connect_to_twitter_endpoint(url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
    
# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def connect_to_spoon_endpoint(url):
    headers = {}
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()