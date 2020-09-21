import flask
import os
import random

app = flask.Flask(__name__)

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

