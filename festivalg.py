#Import flask class + render_template class for acessing html templates Import url_for, for serving static files (css,js)
from flask import Flask, render_template, url_for, request
import mysql.connector
import json

app = Flask(__name__)

#Festival Class
# class festival:
#     def __init__(self, name, description, price, location, date, artists, weather, genre, youtube_showreel,):
#         self.name = name #Manual
#         self.description = description #Manual
#         self.price = price #Manual (add buy link?)
#         self.location = location #Manual
#         self.date = date #Manual
#         self.artists = artists #Nested artist objects
#         self.new_artists = new_artists #difference from old scrape to new scrape
#         self.weather = weather #Weather API
#         self.genre = genre #Manual
#         self.youtube_showreel = youtube_showreel #Manual

# artists class
# class artist:
#     def __init__(self, name, image, genre, description, country, festival, top_tracks,):
#         self.name = name #Webscrape festival site
#         self.image = image #SpotifyAPI
#         self.genre = genre #SpotifyAPI
#         self.description = description #SpotifyAPI (maybe not avaliable?)
#         self.country = country #SpotifyAPi
#         self.festival = festival #Parent Class
#         self.top_tracks = top_tracks #SpotifyApi


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

cur = mydb.cursor()
cur.execute("SELECT name FROM roskildefestival")
result_list = [row[0] for row in cur.fetchall()]
roskildeartists = (json.dumps(result_list))


festivals = [
    {
        'name': 'Roskilde Festival',
        'price': '2900',
        'description': 'Very good festival',
        'location': 'Roskilde',
        'weather': 'Sunny',
        'artists': 'many',
        'genre': 'Everything',
        'date': 'April 20, 2018'
    }
]

artists = [
    {
        'name': 'Bob',
        'image': 'https://i.scdn.co/image/6d869bf0d56329a00bece664e8cd9f92e4fa83d7',
        'country': 'Denmark',
        'genre': 'Hiphop',
        'toptracks': 'toptracks here',
        'festival': 'Roskilde'
    },
    {
        'name': 'Alice',
        'image': 'https://i.scdn.co/image/6d869bf0d56329a00bece664e8cd9f92e4fa83d7',
        'country': 'Denmark',
        'genre': 'Hiphop',
        'toptracks': 'toptracks here',
        'festival': 'Roskilde'
    }
]


# Default route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', roskildeartists=roskildeartists)

#Search route artist
@app.route("/artist", methods=["GET", "POST"])
def artist():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        artists = request.form.get("search")
        return render_template("artist.html", artists=artists)



#Search route festival
@app.route("/festival")
def festival():
    return render_template('festival.html', title='Festival', festivals=festivals)

# @app.route("/artist")
# def artist():
#     return render_template('artist.html', title='Artists', artists=artists)

if __name__ == '__main__':
    app.run(debug=True)
