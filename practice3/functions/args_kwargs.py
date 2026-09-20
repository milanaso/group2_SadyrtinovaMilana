# Here is a function that accepts several favorite foods.
def favorite_foods(*foods, **person):
    print("Favorite foods:", foods)
    print("Name:", person["name"])


# Here is an example using *args and **kwargs.
favorite_foods(
    "Pizza",
    "Burger",
    "Sushi",
    name="Milana"
)
