from collections import Counter

s = "datastructures"
count = Counter(s) #it counts and prints all the repeated elements with numbers
most_common = count.most_common(1) # this will diesplay only 1 word which is most repearted
print(most_common)
print(count)