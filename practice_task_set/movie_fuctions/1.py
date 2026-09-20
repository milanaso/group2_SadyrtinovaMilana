def is_good_movie(movie):
    return movie["imdb"] > 5.5


movie = {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
}

print(is_good_movie(movie))
