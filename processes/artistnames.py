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

# Prints all artists in list (removes white space)
for artist in samples:
    print(list(artist.stripped_strings)[0])

# Check for lenght throw error if empty?? made by echo (i don't get this)
for artist in samples:
x = list(artist.stripped_strings)
if x:
    print(x[0])

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

# Add sql query and values
sql = "INSERT INTO roskildeartists (name) VALUES (%s)"

mycursor.executemany(sql, ??) #How to put entire list into db?

mydb.commit()
