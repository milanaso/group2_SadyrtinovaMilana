def grams_to_ounces(grams):
    return 28.3495231 * grams


def is_palindrome(text):
    return text == text[::-1]

print(grams_to_ounces(10))
print(is_palindrome("madam"))