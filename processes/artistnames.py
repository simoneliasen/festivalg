#Webscraper for Roskilde Festival
import mysql.connector #Import Mysql library
import requests #Import Requests Library
result = requests.get("https://www.roskilde-festival.dk/en/line-up/") #Select page to scrape

#print(result.status_code) #Make sure we got a result (should return 200)
#print(result.headers) #Return header info
#print(result.content) #Returrns all results from page

# Store content in accesible variable
c = result.content

# Start parsing data with Beautifoulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(c, 'xml')
samples = soup.find_all("a", "name")

# Convert artist names into a list
artist_names = []
for artist in samples:
    artist_names.append(list(artist.stripped_strings)[0]) #adds stripped strings to list

#Insert list of elements into Sql database
import mysql.connector

# Database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

mycursor = mydb.cursor()

sql = "INSERT INTO roskildeartists (name) VALUES (%s)"

mycursor.executemany(sql, [[name] for name in artist_names]) #Puts list into db, with each element being own list

mydb.commit()



# Check for lenght throw error if empty?? made by echo (i don't get this)
# x = list(artist.stripped_strings)
# if x:
#     print(x[0])
