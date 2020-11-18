
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys
import flask
import os
import random
import requests
import json
from datetime import datetime, date, time


consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
bearer_token=os.environ["BEARER_TOKEN"]

spoonacular_key=os.environ['SPOON_KEY']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

app = flask.Flask(__name__)

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
    response = connect_to_endpoint(url, headers)
    return response


# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
    


@app.route('/') #python decorator
def index():
    foods = ["Macaroni", "Eggs Benedict", "Chicken Tikka Masala", "Spicy Noodles", "Cake Mug", "Tomato Soup", "Grilled Cheese"]
    #search tweets for random food 
    food = foods[random.randint(0,6)]
    
    twitter_url = create_twitter_url(food)
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    json_response = connect_to_endpoint(twitter_url, headers)

    #parse random tweet for text, author, and date/time
    rand_tweet = random.randint(0,3)
    tweet_data = (json_response["data"][rand_tweet])
    tweet_user = (json_response["includes"]["users"][rand_tweet]["username"])
    tweet_name = (json_response["includes"]["users"][rand_tweet]["name"])
    tweet_text = tweet_data["text"]
    tweet_datetime = datetime.strptime(tweet_data["created_at"], '%Y-%m-%dT%H:%M:%S.000Z')

    #parse random recipe 
    spoon_url = create_spoon_url(food)
    headers = {}
    json_response = connect_to_endpoint(spoon_url, headers)
    
    num_recipes = json_response["totalResults"] if json_response["totalResults"] < 10 else json_response["number"]
    print(num_recipes)
    print(json_response)
    rand_recipe = random.randint(1, num_recipes-1)
    recipe = json_response["results"][rand_recipe]
    recipe_id = recipe["id"]
    recipe_info = getRecipeInfo(recipe_id)
    print(recipe_info)

    ingredients = recipe_info["extendedIngredients"]
    ingredients_len = len(ingredients)

    
    return flask.render_template(
        "index.html",
        food = food,
        tweetText = tweet_text,
        tweetUser = "@"+tweet_user,
        tweetName = tweet_name,
        tweetDatetime = tweet_datetime,
        recipe = recipe,
        recipe_info = recipe_info,
        ingredients = ingredients,
        ingredients_len = ingredients_len
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

