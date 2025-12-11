from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "revmovies"


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username and id then
            session["user_id"] = user["id"]
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


@app.route("/addreview/<movie_id>", methods=["GET", "POST"])
def AddReview(movie_id):

    movieData = db.GetMovie(movie_id)
    # Did they click submit?
    if request.method == "POST":
        title = request.form["title"]
        review_date = request.form["review_date"]
        rating = request.form["rating"]
        review_text = request.form["review_text"]
        user_id = session["user_id"]

        # Send the data to add our new guess to the db
        db.AddReview(title, review_date, rating, review_text, movie_id, user_id)

        reviewsData = db.GetReviews(movie_id)

        return render_template("movie.html", movie=movieData, reviews=reviewsData)

    return render_template("addreview.html", movie=movieData)


@app.route("/editreview/<id>", methods=["GET", "POST"])
def EditReview(id):
    reviewData = db.GetReview(id)
    movieData = db.GetMovie(reviewData["movie_id"])

    if request.method == "POST":
        title = request.form["title"]
        review_date = request.form["review_date"]
        rating = request.form["rating"]
        review_text = request.form["review_text"]
        user_id = session["user_id"]
        db.EditReview(title, review_date, rating, review_text, id)

        reviewsData = db.GetReviews(reviewData["movie_id"])
        return render_template("movie.html", movie=movieData, reviews=reviewsData)

    return render_template("editreview.html", movie=movieData, review=reviewData)


@app.route("/deletereview/<id>")
def DeleteReview(id):
    reviewData = db.GetReview(id)
    movieData = db.GetMovie(reviewData["movie_id"])

    db.DeleteReview(id)

    reviewsData = db.GetReviews(reviewData["movie_id"])
    return render_template("movie.html", movie=movieData, reviews=reviewsData)


@app.route("/addmovie", methods=["GET", "POST"])
def AddMovie():

    # Did they click submit?
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        release_date = request.form["release_date"]
        movie_description = request.form["movie_description"]
        genre = request.form["genre"]
        user_id = session["user_id"]

        # Send the data to add our new movie to the db
        db.AddMovie(movie_name, release_date, movie_description, genre)

        moviesData = db.GetAllMovies()
        return render_template("movie_list.html", movies=moviesData)

    return render_template("addmovie.html")


app.run(debug=True, port=5000)
