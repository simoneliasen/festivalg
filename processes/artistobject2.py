#Webscraper for Roskilde Festival
import mysql.connector #Import Mysql library
import requests #Import Requests Library
from bs4 import BeautifulSoup
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#Webscraper: Roskilde Festival
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") #Select page to scrape
# Store content in accesible variable
c = result.content
# Start parsing data with Beautifoulsoup
soup = BeautifulSoup(c, 'xml')
samples = soup.find_all("a", "name")

# Artist List creation (data cleanup)
artist_names = []
for artist in samples:
    artist_names.append(list(artist.stripped_strings)[0]) #adds stripped strings to list

#Spotify: Client Creditial flow (client_id + client_secret)
client_credentials_manager = SpotifyClientCredentials(client_id='1fc1953f35974811bb2511e360dd422b', client_secret='172b85d4d592449f9268ab7285598088')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get album data from first row in table (test)
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = str(artist_names[0]) #Inserts first item in scraped artist list (test)

#Search spotify with query (q) with artist name, and retrieves name,image,url,genres in list
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    artist_object_data = (((artist['name'], artist['images'][0]['url'], artist['external_urls']['spotify'] )))

# Database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)
#Insert Spotify  data into sql  table
mycursor = mydb.cursor()
mycursor.execute('INSERT INTO roskildefestival (name, image, url) VALUES (%s, %s, %s)', artist_object_data)
mydb.commit()

#THINGS TO ADD/EDIT
#1. Get more data (toptracks, genre, festival, description )
#2. Insert all values into SQL
#3. Check for duplicates (don't store duplicates)
#4. If new artists, from last scrape, store as "new artists"
#5. Set up daily scraping (1-2 times a day)
#6. Add more festival scrapers

#ISSUES
#1. What to do if not on spotify?
