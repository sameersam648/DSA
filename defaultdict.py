from collections import defaultdict
words = ["data", "structures", "stack", "queue", "sorting", "search"]

groups = defaultdict(list)

for word in words:
    first_letter = word[0]
    groups[first_letter].append(word)


for letter, group in groups.items():
    print(letter, " : ", groups)
