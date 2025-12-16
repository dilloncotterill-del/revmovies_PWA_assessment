import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/revmovies.db")
    db.row_factory = sqlite3.Row

    return db


def GetAllMovies():

    # Connect, select all movies and fetch them
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

    # Checks if they exist
    if user is not None:
        # If they exist, also checks if their password is correct
        if check_password_hash(user["password"], password):
            # If correct, return their details
            return user

    # If the password or username fails, returns None
    return None


def RegisterUser(username, password):

    # Check if they entered a username or a password
    if username is None or password is None:
        return False

    db = GetDB()
    hash = generate_password_hash(password)
    # Adds them to the database
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
    # Gets a movie that has the matching id that is passed in
    movie = db.execute("SELECT * FROM Movies WHERE id=?", (id,)).fetchone()
    db.close()
    return movie


def GetReviews(id):
    db = GetDB()
    # Selects all reviews, joins reviews and users where the users id value is the same as the reviews id value
    reviews = db.execute(
        "SELECT Reviews.id as id, title, review_date, rating, review_text, movie_id, username FROM Users JOIN Reviews ON Users.ID=Reviews.user_id;",
    ).fetchall()
    db.close()
    return reviews


def GetReview(id):
    db = GetDB()
    # Gets reviews that have a matching id to the one that is passed in
    review = db.execute("SELECT * FROM Reviews WHERE id=?", (id,)).fetchone()
    db.close()
    return review


def AddReview(title, review_date, rating, review_text, movie_id, user_id):

    # Checks if the date or title are nothing
    if review_date is None or title is None:
        return False

    # find the db and insert the new review
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

    # get the db and update the review based on what the user inputs
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

    # removes a movie that has a matching id to the one passed in
    db = GetDB()
    db.execute(
        "DELETE From Reviews WHERE id=?",
        (id,),
    )
    db.commit()

    return True


def AddMovie(movie_name, release_date, movie_description, genre):

    # checks if any fields are empty, returns false
    if (
        movie_name is None
        or release_date is None
        or movie_description is None
        or genre is None
    ):
        return False

    # inserts the users chosen movie into the movie database
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
