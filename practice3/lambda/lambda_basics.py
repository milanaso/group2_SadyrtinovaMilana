# Here is a lambda function that calculates a 10% discount.
calculate_discount = lambda price: price * 0.9

# Here is the original product price.
product_price = 10000

# Here is the price after applying the discount.
discounted_price = calculate_discount(product_price)
print("Original price:", product_price)
print("Price after discount:", discounted_price)
