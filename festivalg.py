#Import flask class + render_template class for acessing html templates Import url_for, for serving static files (css,js)
from flask import Flask, render_template, url_for, request
import mysql.connector
import json

app = Flask(__name__)

# Mysql connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

# display Mysql names for search autocomplete
cur = mydb.cursor()
cur.execute("SELECT name FROM roskildefestival")
result_list = [row[0] for row in cur.fetchall()]
roskildeartists = (json.dumps(result_list))

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', roskildeartists=roskildeartists)

# Artist page
@app.route('/artist', methods=["GET", "POST"])
def artist(): #If Attempt to GET is made, display error
    if request.method == "GET":
              return "Please submit the form instead."
    else: # Takes input from searchbar to variable artist
        artist = request.form['search']
        return render_template("artist.html", artist = artist)

if __name__ == '__main__':
    app.run(debug=True)
