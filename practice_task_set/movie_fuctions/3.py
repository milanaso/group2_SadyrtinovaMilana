def movies_by_category(movies, category):
    result = []

    for movie in movies:
        if movie["category"] == category:
            result.append(movie)

    return result

