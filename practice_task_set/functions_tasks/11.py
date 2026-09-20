def is_palindrome(text):
    text = text.lower().replace(" ", "")

    return text == text[::-1]


text = input()

print(is_palindrome(text))
