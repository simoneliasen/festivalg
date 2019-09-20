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


# Old Mysql code to search names of artists
#cur = mydb.cursor()
#cur.execute("SELECT name FROM roskildefestival")

# artistlist = session.query(SomeModel.col1)
#result_list = [row[0] for row in cur.fetchall()]
#roskildeartists = (json.dumps(result_list))

# Momentary search results until postgres is set up properly
List = ["Geeks", "For", "Geeks"] 
roskildeartists = (json.dumps(List))

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', roskildeartists=roskildeartists)

# Artist page
@app.route('/artist', methods=["GET", "POST"])
def artist():
    if request.method == "GET":
              return "Please submit the form instead."
    else:
        print('Close enough')
        #Input from form
 #       search_input = request.form.get("search")
        #Use data from database
  #      cur = mydb.cursor()
   #     cur.execute("SELECT * FROM roskildefestival WHERE name = %s", (search_input,))
    #    artist_data = cur.fetchall()
     #   return render_template("artist.html", search_input = search_input, artist_data = artist_data)

if __name__ == '__main__':
    app.run(debug=True)


