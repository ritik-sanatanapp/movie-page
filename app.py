from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import json
from flask import abort

app = Flask(__name__)
MOVIES_DIR = "movies"

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
movies_collection  = db["movies"]
common_collection = db["common"] 


# ------------------ LOAD COMMON ------------------
def load_common():
    return common_collection.find_one({}, {"_id": 0})

# ------------------ LOAD MOVIE -------------------
def load_movie(movie_id, lang="en"):
    full_id = f"{movie_id}-{lang}"
    movie = movies_collection.find_one(
        {"id": full_id},
        {"_id": 0}
    )
    if not movie:
        # fallback to English
        movie = movies_collection.find_one(
            {"id": f"{movie_id}-en"},
            {"_id": 0}
        )

    return movie if movie else {}

# ------------------ LANGUAGE ---------------------
def get_lang():
    """Get language from query param, default 'en'"""
    lang = request.args.get("lang", "en")
    return lang if lang in ["en", "hi"] else "en"

# ------------------ HOME -------------------------
@app.route("/")
def home():
    lang = get_lang()
    common = load_common()
    movie = load_movie("kalyug", lang)  # default movie
    return render_template("movie.html", common=common, movie=movie, lang=lang)


# ------------------ ALL MOVIE PAGE -------------------
@app.route("/movies")
def all_movies():
    lang = get_lang()
    common = load_common()
    movies = list(movies_collection.find(
        {"id": {"$regex": f"-{lang}$"}},   # ✅ match kalyug-hi
        {"_id": 0}
    ))
    return render_template(
        "all_movies.html",
        common=common,
        movies=movies,
        lang=lang
    )
# ------------------ MOVIE PAGE -------------------
@app.route("/movies/<movie_id>")
def movie_page(movie_id):
    lang = get_lang()
    common = load_common()
    movie = load_movie(movie_id, lang)
    if not movie:
        abort(404)  
    return render_template(
    "movie.html",
    common=common,  
    movie=movie,
    lang=lang
)
# ------------------ RUN --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)  