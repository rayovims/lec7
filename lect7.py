import flask
import os
import random

app = flask.Flask(__name__)

# Python decorator 
@app.route('/') 
def index():
    artists = ["drake", "quavo", "bad bunny", "anuel AAA", "jon bellion"]
    images = ["/static/drake.jpg", "/static/quavo.jpg", "/static/bad-bunny.jpg", "/static/Anuel.jpg", "/static/jon.jpg"]
    return flask.render_template(
        "index.html",
        len = len(artists),
        Artists = artists,
        Images = images
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)