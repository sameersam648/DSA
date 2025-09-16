from collections import Counter

s = "datastructures"
counter = Counter(s)

most_common_letter = counter.most_common(1)
print(most_common_letter)

#just did it at first attempt after reading from gpt