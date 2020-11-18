# project1-cpd24

## Step to deploy the app
0. Sign up for the twitter developer portal at https://developer.twitter.com
1. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
2. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    If needed, you can regenerate your access token and secret.
3. Run the following in your terminal:
    sudo pip install tweepy
    (or) sudo pip3 install tweepy
    (or) pip install tweepy
    (or) pip3 install tweepy
4. Install flask using the same process as above ([sudo] pip[3] install flask)
5. Add your secret keys (from step 2) by making a new root-level file called twitter.env and populating it as follows:
    export CONSUMER_KEY=''
    export CONSUMER_KEY_SECRET=''
    export ACCESS_TOKEN=''
    export ACCESS_TOKEN_SECRET=''
    export BEARER_TOKEN=''
6. Run `python main.py`
    You may want to add the secret keys (from step 2) as environment variables by clicking ENV in the running project terminal
7. If on Cloud9, preview templates/index.html. This should successfully render the HTML!
#### Run on Heroku
8. Sign up for heroku at heroku.com 
9. Install heroku by running `npm install -g heroku`
10. Go through the following steps:
    `heroku login -i`
    `heroku create`
    `git push heroku master`
11. Navigate to your newly-created heroku site!
12. Add your secret keys (from tweepy.env) by going to https://dashboard.heroku.com/apps
    and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
    "Reveal Config Vars" and add the key value pairs for each variable in user_tweets.py
    Your config var key names should be:
    CONSUMER_KEY
    CONSUMER_KEY_SECRET
    ACCESS_TOKEN
    ACCESS_TOKEN_SECRET
    BEARER_TOKEN
13. Configure requirements.txt with all requirements needed to run your app.
14. Configure Procfile with the command needed to run your app.
15. If you are still having issues, you may use `heroku logs --tail` to see what's wrong.

## Problems
1. Parsing the date/time from the twitter json caused some confusion simply because I was unfamiliar of the format returned. A sample date/time returned from a tweet is: 2020-07-06T04:11:35.000Z. There wasn't any documentation for what the .000Z was. After a quick google search determined it was the [milliseconds and timezone](https://stackoverflow.com/questions/16151383/what-does-the-000z-of-yyyy-mm-ddt000000-000z-mean#:~:text=73,and%20Z%20indicates%20UTC%20timezone.). If I had more time, I would make the date and time of the tweet look better

 ## Technical Issues
 1. At one point I was getting errors because I confused which version of the API I was using. v1.1 and v2 have different query urls
    v1.1: `https://api.twitter.com/1.1/search/tweets.json` followed by q={keywords}
    v2: `https://api.twitter.com/2/tweets/search/recent` followed by query={keywords}
    You'll notice each version has different query parameters as well. 
    Read more for v1.1: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
    Read more for v2: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent#requests
    
    
2. One problem I had was connecting to Heroku. I got an error that Heroku could not detect my buildpack. To resolve this, I first tried adding the python pack through the settings in the dashboard. This did not work for me, so then I added it manually via the command line. 
    `heroku buildpacks:set heroku/python`
    
 3. In order to query the user object, I needed to specify an expansion in the url. For this, I found this page in the doc that helped clarify what expansions were: https://developer.twitter.com/en/docs/twitter-api/expansions
    In my url, I added `expansions=author_id` to get the user data. 

## Additional Future Features
1. Add the user's profile picture to the tweet. I would do this by following these instructions: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners
    In short, the user object has a field `profile_image_url` which I would pass to the html and display in <img/> tags.
    
2. I would try to match the tweet search more closely with the recipe generated. To do this, I would first generate the random food from spoonacular, get the title, and use the title to search for relevant tweets. 

