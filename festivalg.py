#Import flask class + render_template class for acessing html templates Import url_for, for serving static files (css,js)
from flask import Flask, render_template, url_for
app = Flask(__name__)


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
    },
    {
        'name': 'Northside',
        'price': '1800',
        'description': 'Very good festival',
        'location': 'Aarhus',
        'weather': 'Sunny',
        'artists': 'many',
        'genre': 'Everything',
        'date': 'April 25, 2018'
    }
]

artists = [
    {
        'name': 'Asap Rocky Impala',
        'description': 'very cool',
        'country': 'Norway',
        'genre': 'Hiphop',
        'toptracks': 'toptracks here',
        'festival': 'Roskilde'
    },
    {
        'name': 'Tame Impala',
        'description': 'good stuff',
        'country': 'Denmark',
        'genre': 'Pop',
        'toptracks': 'toptracks here',
        'festival': 'Northside'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', festivals=festivals)

@app.route("/festival")
def festival():
    return render_template('festival.html', title='Festival', festivals=festivals)

@app.route("/artist")
def artist():
    return render_template('artist.html', title='Artists', artists=artists)

if __name__ == '__main__':
    app.run(debug=True)
