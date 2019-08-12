import mysql.connector 
import requests 
from bs4 import BeautifulSoup
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#Webscraper: Roskilde Festival
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") 
c = result.content
soup = BeautifulSoup(c, 'xml')
samples = soup.find_all("a", "name")

# List of artists (data cleanup from webscrape)
artist_names = []
for artist in samples:
    artist_names.append(list(artist.stripped_strings)[0]) #adds stripped strings to list

#Spotify: Client Creditial flow (client_id + client_secret)
client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Search spotify with query (q) from previous list of artists, and retrieves additional data
roskildefestival = []
artists = []
uri = []
for element in artist_names:
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = element
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
        artist_object_data = (((artist['name'], artist['external_urls'])))
        artists.append(artist_object_data[0])
        uri.append(artist_object_data[1]['spotify'])       
roskildefestival = list(zip(artists,uri))

# Database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)
mycursor = mydb.cursor()
sql = "INSERT INTO roskildefestival (name, url) VALUES (%s, %s)"
mycursor.executemany(sql, roskildefestival)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# To do
# Register all artists
# Append img and uri where artist == artist in db
# Check for doubles
# What to show if img isn't avaliable
# If artist already exsist, don't append