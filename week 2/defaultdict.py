from collections import defaultdict

words = ["data", "structures", "science", "stack", "queue"]

grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))


#i didn't get the complete idea of it >>>