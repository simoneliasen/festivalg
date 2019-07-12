# List of artists (data cleanup from webscrape)
artist_names = ['Cool artist', 'another cool artist', 'another one']

name = str(artist_names[0]) #First item of list

# Spotify request for additional data on artist
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    artist_object_data = (((artist['name'], artist['images'][0]['url'], artist['external_urls']['spotify'] )))


# Database connection 
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
