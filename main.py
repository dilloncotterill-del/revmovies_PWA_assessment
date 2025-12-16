from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "revmovies"


@app.route("/")
def Home():
    # when on homepage, renders its html page and text
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Did their details match any in the system
        user = db.CheckLogin(username, password)
        if user:
            # If so, save their username and id in the session
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            # Send them back to the homepage
            return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def Logout():
    # if user logs out, clears their session details
    session.clear()
    return redirect("/")


@app.route("/movie_list")
def Movie_list():
    moviesData = db.GetAllMovies()
    # if user goes to the movie list, renders its html page and defines movies so that it can be used in this page
    return render_template("movie_list.html", movies=moviesData)


@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, registers them as a new user
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Attempt to add them to the DB
        if db.RegisterUser(username, password):
            # Successful registration, redirects to homepage
            return redirect("/")

    # unsuccesful registration keeps them on the register page
    return render_template("register.html")


@app.route("/movie/<id>")
def Movie(id):
    movieData = db.GetMovie(id)
    # sets the movie and reviews data
    reviewsData = db.GetReviews(id)

    return render_template("movie.html", movie=movieData, reviews=reviewsData)


@app.route("/addreview/<movie_id>", methods=["GET", "POST"])
def AddReview(movie_id):

    if session.get("user_id") == None:
        return redirect("/")

    movieData = db.GetMovie(movie_id)
    # Did user click submit
    if request.method == "POST":
        title = request.form["title"]
        review_date = request.form["review_date"]
        rating = request.form["rating"]
        review_text = request.form["review_text"]
        user_id = session["user_id"]

        # Send data to add new review to the DB of reviews
        db.AddReview(title, review_date, rating, review_text, movie_id, user_id)

        reviewsData = db.GetReviews(movie_id)

        # returns them to the specific movie page
        return render_template("movie.html", movie=movieData, reviews=reviewsData)

    return render_template("addreview.html", movie=movieData)


@app.route("/editreview/<id>", methods=["GET", "POST"])
def EditReview(id):

    if session.get("user_id") == None:
        # prevents the user from accessing the page if they are not registered and logged in
        return redirect("/")

    reviewData = db.GetReview(id)
    movieData = db.GetMovie(reviewData["movie_id"])

    if request.method == "POST":
        # checks if they have clicked submit, and if so changes the values of each part of the review
        title = request.form["title"]
        review_date = request.form["review_date"]
        rating = request.form["rating"]
        review_text = request.form["review_text"]
        user_id = session["user_id"]
        db.EditReview(title, review_date, rating, review_text, id)

        reviewsData = db.GetReviews(reviewData["movie_id"])
        # returns them to the movie specific page
        return render_template("movie.html", movie=movieData, reviews=reviewsData)

    return render_template("editreview.html", movie=movieData, review=reviewData)


@app.route("/deletereview/<id>")
def DeleteReview(id):

    # prevents the user from accessing the page if they are not registered and logged in
    if session.get("user_id") == None:
        return redirect("/")

    reviewData = db.GetReview(id)
    movieData = db.GetMovie(reviewData["movie_id"])

    # calls delete review to get rid of it
    db.DeleteReview(id)

    reviewsData = db.GetReviews(reviewData["movie_id"])
    return render_template("movie.html", movie=movieData, reviews=reviewsData)


@app.route("/addmovie", methods=["GET", "POST"])
def AddMovie():

    # checks if they have clicked submit, and if so changes the values of each part of the review
    if session.get("user_id") == None:
        return redirect("/")

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
