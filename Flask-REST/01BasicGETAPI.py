from flask import Flask

app=Flask(__name__)

# http://127.0.0.1:5000/film
@app.route('/film',methods=['GET'])
def get_filmdata():
    film={
        "name":"sholay",
        "year":1975,
        "genre":"action",
        "language":"hindi",
        "director":"ramesh sippy",
        "actor":["sanjeev kumar","dharmendra","amitabh bachchan"],
        "actress":["jaya","hema"],
        "music":"r d burman",
        "imdbrating":8.3
    }
    return film

app.run(debug=True)