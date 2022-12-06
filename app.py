from flask import Flask, render_template, request
import bqclient


# Backend
def recommendStrategy(genre, artist):
    # based on the query(a list of names of music), generate a list of music, and return it
    client = bqclient.create_bqclient("setup/key-file.json")
    res = bqclient.run_query(client, genre)
    print(res)
    # todo: implement recommend strategy here
    # connect db, and query from database, talk with guys responsible for part 1
    return res["track_name"].values  # a list of music including/related to the keyword


# Frontend
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        artist = request.form['artist']
        genre = request.form['genre']
        result = recommendStrategy(artist, genre)
        return render_template("result.html", result=result)


app.run(debug=True)
