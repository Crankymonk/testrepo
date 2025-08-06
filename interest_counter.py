from collections import Counter

interests = [
    (0, "hadoop"), (0, "Java"),
    (1, "hadoop"), (1, "Java"),
    (2, "big data"), (2, "Java"),
    (2, "hadoop"), (2, "Python"),
]

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split()
                           )

print(words_and_counts)
