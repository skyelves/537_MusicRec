from flask import Flask, render_template, request
import bqclient


# Backend
def recommendStrategy(artist, genre, number):
    # based on the query(a list of names of music), generate a list of music, and return it
    res = bqclient.run_query(client, artist, genre, number)
    # todo: implement recommend strategy here
    # connect db, and query from database, talk with guys responsible for part 1
    return res  # a list of music including/related to the keyword


# Frontend
app = Flask(__name__)
client = bqclient.create_bqclient("setup/key-file.json")


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        artist = request.form['artist']
        genre = request.form['genre']
        number = request.form['number']
        result = recommendStrategy(artist, genre, number)
        return render_template("result.html", result=result)


app.run(debug=True)