from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from sqlalchemy.orm import sessionmaker
import json
import os
import psycopg2
#Add for local development
#import OpenSSL


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

#HTTPS redirect
@app.before_request
def before_request():
    if not request.is_secure and app.env != "development":
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)

#404-page
@app.errorhandler(404)
def page_not_found(error):
   return render_template('index.html', title = '404'), 404

# Home page
@app.route('/', methods=['GET'])
def home():
    momentarystorage = []
    artists = Artist.query.all()
    for artist in artists:
        momentarystorage.append(artist.name)
        momentarystorage.append(artist.festival)
    distinctvalues = set(momentarystorage)
    distinctlist = list(distinctvalues)
    artistnames = (json.dumps(distinctlist))
    return render_template('index.html', artistnames=artistnames)
 
@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')



# Artist page
@app.route('/artist', methods=["GET", "POST"])
def artist():
    if request.method == "GET":
              return "Please submit the form instead."
    else:
        search_input = request.form.get("search")
        artist_data = Artist.query.filter_by(name=search_input)
        festival_data = Artist.query.filter_by(festival=search_input)
        for data in artist_data:
            if data in artist_data:
                return render_template("artist.html", search_input = search_input, artist_data = artist_data)
        for element in festival_data:
            if element in festival_data:
                return render_template("festival.html", search_input = search_input, festival_data = festival_data)
        else:
            message = "No artist or festival matched your input"
            return message
    

if __name__ == '__main__':
    #app.run(debug=True)

#Add for local development
    app.run(debug=True, ssl_context='adhoc')



