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
    movieData = db.GetAllMovies()
    return render_template("movie_list.html", movies=movieData)


app.run(debug=True, port=5000)
