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

## Problems
1. I came across a problem where my styles.css file was not rendering despite linking in my html. The following steps failed to render my css:
    i) create a file styles.css inside static directory
    ii) insert the styles (copy and paste what I currently have in the <style/> tags in index.html)
    iii) link the style sheet to my html inside the `<head/>` tags
      `<link rel="stylesheet" href="static/styles.css">`
    iii) re-run and preview the app
  My solution was to just add my css to index.html in the header using `<style/>` tags. 
  
 ## Technical Issues
 1. At one point I was getting errors because I confused which version of the API I was using. v1.1 and v2 have different query urls
    v1.1: `https://api.twitter.com/1.1/search/tweets.json` followed by q={keywords}
    v2: `https://api.twitter.com/2/tweets/search/recent` followed by query={keywords}
    You'll notice each version has different query parameters as well. 
    Read more for v1.1: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
    Read more for v2: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent#requests
    
 2. Parsing the date/time caused some confusion because I didn't know what the last part of the format was. A sample date/time returned from a tweet is: 2020-07-06T04:11:35.000Z
    There wasn't any documentation for what the .000Z was, a d quick search determined it was the milliseconds and timezone. I decided that this information wasn't needed for this project
    
 3. In order to query the user object, I needed to specify an expansion in the url. For this, I found this page in the doc that helped clarify what expansions were: https://developer.twitter.com/en/docs/twitter-api/expansions
    In my url, I added `expansions=author_id` to get the user data. 

# Additional Future Features
1. Add the user's profile picture to the tweet. I would do this by following these instructions: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/user-profile-images-and-banners
    In short, the user object has a field `profile_image_url` which I would pass to the html and display in <img/> tags.
