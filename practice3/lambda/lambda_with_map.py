# Here is a list of product prices.
prices = [1000, 2500, 5000, 7500, 10000]

# Here is map() adding 12% tax to every price.
prices_with_tax = list(
    map(lambda price: price * 1.12, prices)
)
print("Original prices:", prices)
print("Prices with tax:", prices_with_tax)
