def average_imdb(movies):
    total = 0

    for movie in movies:
        total += movie["imdb"]

    return total / len(movies)

