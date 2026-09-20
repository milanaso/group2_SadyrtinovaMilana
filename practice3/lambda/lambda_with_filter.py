# Here is a list of student scores.
scores = [45, 67, 89, 52, 95, 38, 76]

# Here is filter() selecting only passing scores.
passing_scores = list(
    filter(lambda score: score >= 60, scores)
)
print("All scores:", scores)
print("Passing scores:", passing_scores)
