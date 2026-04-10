from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
MOVIES_DIR = "movies"

# ------------------ LOAD COMMON ------------------
def load_common():
    with open("./static/common/common.json", encoding="utf-8") as f:
        return json.load(f)

# ------------------ LOAD MOVIE -------------------
def load_movie(movie_id, lang="en"):
    """Load movie JSON for given ID and language"""
    path = f'{MOVIES_DIR}/{movie_id}/data/{lang}.json'
    if not os.path.exists(path):
        path = f'{MOVIES_DIR}/{movie_id}/data/en.json'  # fallback to English
    with open(path, encoding="utf-8") as f:
        return json.load(f)

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

# ------------------ MOVIE PAGE -------------------
@app.route("/movie/<movie_id>")
def movie_page(movie_id):
    lang = get_lang()
    common = load_common()
    movie = load_movie(movie_id, lang)
    return render_template(
    "movie.html",
    common=common,  
    movie=movie,
    lang=lang
)
# ------------------ RUN --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)