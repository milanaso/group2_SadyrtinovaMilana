def movies_by_category(movies, category):
    result = []

    for movie in movies:
        if movie["category"] == category:
            result.append(movie)

    return result

def average_imdb(movies):
    total = 0

    for movie in movies:
        total += movie["imdb"]

    return total / len(movies)

def category_average(movies, category):
    category_movies = movies_by_category(movies, category)

    if len(category_movies) == 0:
        return 0

    return average_imdb(category_movies)
