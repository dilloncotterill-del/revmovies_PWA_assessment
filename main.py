from flask import Flask, render_template, request
import db

app = Flask(__name__)
app.secret_key = "revmovies"


@app.route("/")
def Home():
    return render_template("base.html")


@app.route("/movie_list")
def Movie_list():
    movieData = db.GetAllMovies()
    return render_template("movie_list.html", movies=movieData)


app.run(debug=True, port=5000)
