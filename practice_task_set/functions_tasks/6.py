def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


sentence = input()

print(reverse_words(sentence))
