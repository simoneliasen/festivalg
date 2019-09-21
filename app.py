from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from sqlalchemy.orm import sessionmaker
import json
import os
import psycopg2
from models import Artist

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Home page
@app.route("/")
@app.route("/home")
def home():
    momentarystorage = []
    artists = Artist.query.all()
    for artist in artists:
        momentarystorage.append(artist.name)
    roskildeartists = (json.dumps(momentarystorage))
    return render_template('home.html', roskildeartists=roskildeartists)

# Artist page
@app.route('/artist', methods=["GET", "POST"])
def artist():
    if request.method == "GET":
              return "Please submit the form instead."
    else:
        search_input = request.form.get("search")
        artist_data = Artist.query.filter_by(name=search_input)
        return render_template("artist.html", search_input = search_input, artist_data = artist_data)

if __name__ == '__main__':
    app.run(debug=True)


