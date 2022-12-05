from flask import Flask, render_template, request
import bqclient


# Backend
def recommendStrategy(keyword):
    # based on the query(a list of names of music), generate a list of music, and return it
    client = bqclient.create_bqclient("key-file.json")
    res = bqclient.run_query(client, keyword)["track_name"].values
    print(res)
    # todo: implement recommend strategy here
    # connect db, and query from database, talk with guys responsible for part 1
    return res  # a list of music including/related to the keyword


# Frontend
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        keyword = request.form['Keyword']
        result = recommendStrategy(keyword)
        return render_template("result.html", result=result)


app.run(debug=True)
