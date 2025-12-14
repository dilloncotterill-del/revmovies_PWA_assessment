import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/revmovies.db")
    db.row_factory = sqlite3.Row

    return db


def GetAllMovies():

    # Connect, query all guesses and then return the data
    db = GetDB()
    movies = db.execute("SELECT * FROM Movies").fetchall()
    db.close()
    return movies


def CheckLogin(username, password):

    db = GetDB()

    # Ask the database for a single user matching the provided name
    user = db.execute(
        "SELECT * FROM Users WHERE username=? COLLATE NOCASE", (username,)
    ).fetchone()

    # Do they exist?
    if user is not None:
        # OK they exist, is their password correct
        if check_password_hash(user["password"], password):
            # They got it right, return their details
            return user

    # If we get here, the username or password failed.
    return None


def RegisterUser(username, password):

    # Check if they gave us a username and password
    if username is None or password is None:
        return False

    # Attempt to add them to the database
    db = GetDB()
    hash = generate_password_hash(password)
    db.execute(
        "INSERT INTO Users(username, password) VALUES(?, ?)",
        (
            username,
            hash,
        ),
    )
    db.commit()

    return True


def GetMovie(id):
    db = GetDB()
    movie = db.execute("SELECT * FROM Movies WHERE id=?", (id,)).fetchone()
    db.close()
    return movie


def GetReviews(id):
    db = GetDB()
    reviews = db.execute(
        "SELECT Reviews.id as id, title, review_date, rating, review_text, movie_id, username FROM Users, Reviews WHERE Users.ID=Reviews.user_id;",
    ).fetchall()
    db.close()
    return reviews


def GetReview(id):
    db = GetDB()
    review = db.execute("SELECT * FROM Reviews WHERE id=?", (id,)).fetchone()
    db.close()
    return review


def AddReview(title, review_date, rating, review_text, movie_id, user_id):

    # Check if any boxes were empty
    if review_date is None or title is None:
        return False

    # Get the DB and add the review
    db = GetDB()
    db.execute(
        "INSERT INTO Reviews(title, review_date, rating, review_text, movie_id, user_id) VALUES (?, ?, ?, ?, ?, ?)",
        (
            title,
            review_date,
            rating,
            review_text,
            movie_id,
            user_id,
        ),
    )
    db.commit()

    return True


def EditReview(title, review_date, rating, review_text, id):

    db = GetDB()
    db.execute(
        "UPDATE Reviews SET title = ?, review_date = ?, rating = ?, review_text = ? WHERE id = ?",
        (
            title,
            review_date,
            rating,
            review_text,
            id,
        ),
    )
    db.commit()

    return True


def DeleteReview(id):

    db = GetDB()
    db.execute(
        "DELETE From Reviews WHERE id=?",
        (id,),
    )
    db.commit()

    return True


def AddMovie(movie_name, release_date, movie_description, genre):

    if (
        movie_name is None
        or release_date is None
        or movie_description is None
        or genre is None
    ):
        return False

    db = GetDB()
    db.execute(
        "INSERT INTO Movies(movie_name, release_date, movie_description, genre) VALUES (?, ?, ?, ?)",
        (
            movie_name,
            release_date,
            movie_description,
            genre,
        ),
    )
    db.commit()

    return True
