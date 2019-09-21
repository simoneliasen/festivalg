from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from sqlalchemy.orm import sessionmaker
import json
import os
import psycopg2

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    festival = db.Column(db.String())
    img = db.Column(db.String())
    uri = db.Column(db.String())
  
    def __repr__(self):
        return f"Artist('{self.name}', '{self.festival}', '{self.image}', '{self.uri}')"

# Home page
@app.route("/")
@app.route("/home")
def home():
    momentarystorage = []
    artists = Artist.query.all.distinct()
    for artist in artists:
        momentarystorage.append(artist.name)
        momentarystorage.append(artist.festival)
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

#Festival page
@app.route('/festival', methods=["GET", "POST"])
def festival():
    if request.method == "GET":
              return "Please submit the form instead."
    else:
        search_input = request.form.get("search")
        artist_data = Artist.query.filter_by(festival=search_input)
        return render_template("festival.html", search_input = search_input, artist_data = artist_data)


if __name__ == '__main__':
    app.run(debug=True)



