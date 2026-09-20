def good_movies(movies):
    result = []

    for movie in movies:
        if movie["imdb"] > 5.5:
            result.append(movie)

    return result
