from flask import Flask, render_template, request, abort
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
movies_collection  = db["movies"]
common_collection = db["common"] 


# ------------------ LOAD COMMON ------------------
def load_common(lang="en"):
    return common_collection.find_one({
        "_id": f"common-{lang}"
    })
# ------------------ LOAD MOVIE -------------------
def load_movie(movie_id, lang="en"):
    full_id = f"{movie_id}-{lang}"
    movie = movies_collection.find_one(
        {"_id": full_id}
    )
    if not movie:
        # fallback to English
        movie = movies_collection.find_one(
            {"_id": f"{movie_id}-en"},
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

    common = load_common(lang)
    movie = load_movie("kalyug", lang)

    return render_template(
        "movie.html",
        common=common,
        movie=movie,
        lang=lang
    )
# ------------------ ALL MOVIE PAGE -------------------
@app.route("/movies")
def all_movies():
    lang = get_lang()
    common = load_common(lang)  
    movies = list(movies_collection.find(
        {"lang": lang}
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
    common = load_common(lang)    
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