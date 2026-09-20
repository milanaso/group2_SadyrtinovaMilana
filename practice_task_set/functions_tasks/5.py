from itertools import permutations


def print_permutations(text):
    for item in permutations(text):
        print("".join(item))


text = input()
print_permutations(text)
