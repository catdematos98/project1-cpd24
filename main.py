
from datetime import datetime, date, time, timedelta
from collections import Counter
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys
import flask
import os
import random
import requests
import json

consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
bearer_token=os.environ["BEARER_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

app = flask.Flask(__name__)

# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def create_url():
    query = "from:twitterdev -is:retweet"
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

# From Twitter example code: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
    

url = create_url()
headers = {"Authorization": "Bearer {}".format(bearer_token)}
json_response = connect_to_endpoint(url, headers)
print(json.dumps(json_response, indent=4, sort_keys=True))

@app.route('/') #python decorator
def index():
    num = random.randint(1, 20)
    return flask.render_template(
        "index.html",
        random_number = num 
        )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

