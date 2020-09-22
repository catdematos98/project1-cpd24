
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

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

app = flask.Flask(__name__)

foods = ["Macaroni", "Eggs Benedict", "Chicken Tikka Masala", "Spicy Noodles", "Cake Mug", "Tomato Soup", "Grilled Cheese"]

# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def create_url(rand_food):
    query = rand_food
    tweet_fields = "created_at,lang"
    user_fields = "username,name"
    url = "https://api.twitter.com/2/tweets/search/recent?expansions=author_id&query={}&tweet.fields={}&user.fields={}".format(
        query, tweet_fields, user_fields
    )
    return url

# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
    


@app.route('/') #python decorator
def index():
    #search tweets for random food 
    food = foods[random.randint(0,6)]
    url = create_url(food)
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    json_response = connect_to_endpoint(url, headers)
    tweets = json.dumps(json_response, indent=4, sort_keys=True)
    
    #parse random tweet for text, author, and date/time
    rand_tweet = random.randint(0,3)
    tweet_data = (json_response["data"][rand_tweet])
    tweet_user = (json_response["includes"]["users"][rand_tweet]["username"])
    tweet_name = (json_response["includes"]["users"][rand_tweet]["name"])
    tweet_text = tweet_data["text"]
    tweet_datetime = datetime.strptime(tweet_data["created_at"], '%Y-%m-%dT%H:%M:%S.000Z')
    
    return flask.render_template(
        "index.html",
        food = food,
        tweetText = tweet_text,
        tweetUser = "@"+tweet_user,
        tweetName = tweet_name,
        tweetDatetime = tweet_datetime
        )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

