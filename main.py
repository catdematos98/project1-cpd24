import sys
import flask
import os
import random
import json
from datetime import datetime, date, time
import api_calls


app = flask.Flask(__name__)



@app.route('/') #python decorator
def index():
    api_calls.auth()
    foods = ["Macaroni", "Eggs Benedict", "Chicken Tikka Masala", "Spicy Noodles", "Cake Mug", "Tomato Soup", "Grilled Cheese"]
    #search tweets for random food 
    food = foods[random.randint(0,6)]
    
    twitter_url = api_calls.create_twitter_url(food)
    json_response = api_calls.connect_to_twitter_endpoint(twitter_url)

    #parse random tweet for text, author, and date/time
    rand_tweet = random.randint(0,3)
    tweet_data = (json_response["data"][rand_tweet])
    tweet_user = (json_response["includes"]["users"][rand_tweet]["username"])
    tweet_name = (json_response["includes"]["users"][rand_tweet]["name"])
    tweet_text = tweet_data["text"]
    tweet_datetime = datetime.strptime(tweet_data["created_at"], '%Y-%m-%dT%H:%M:%S.000Z')

    #parse random recipe 
    spoon_url = api_calls.create_spoon_url(food)
    json_response = api_calls.connect_to_spoon_endpoint(spoon_url)
    
    num_recipes = json_response["totalResults"] if json_response["totalResults"] < 10 else json_response["number"]
    print(num_recipes)
    print(json_response)
    rand_recipe = random.randint(1, num_recipes-1)
    recipe = json_response["results"][rand_recipe]
    recipe_id = recipe["id"]
    recipe_info = api_calls.getRecipeInfo(recipe_id)
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

