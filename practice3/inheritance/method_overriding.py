# Here is the parent class.
class Product:

    # Here is a method that returns the product price.
    def get_price(self, price):
        return price


# Here is the child class.
class DiscountProduct(Product):

    # Here is the overridden method.
    def get_price(self, price):
        return price * 0.9


# Here are objects of both classes.
product = Product()
discount_product = DiscountProduct()

# Here is the original price.
print("Original price:", product.get_price(1000))

# Here is the price after a 10% discount.
print("Discount price:", discount_product.get_price(1000))
