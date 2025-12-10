from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "revmovies"


@app.route("/")
def Home():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username and id then
            session["id"] = user["id"]
            session["username"] = user["username"]

            # Send them back to the homepage
            return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")


@app.route("/movie_list")
def Movie_list():
    moviesData = db.GetAllMovies()
    return render_template("movie_list.html", movies=moviesData)


@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            # Success! Let's go to the homepage
            return redirect("/")

    return render_template("register.html")


@app.route("/movie/<id>")
def Movie(id):
    movieData = db.GetMovie(id)
    reviewsData = db.GetReviews(id)

    return render_template("movie.html", movie=movieData, reviews=reviewsData)


app.run(debug=True, port=5000)
