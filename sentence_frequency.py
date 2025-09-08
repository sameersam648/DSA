sentence = "the cat sat on the mat with the cat"
#split the sectence into words
words = sentence.split(" ")

#creating the empty dictionary
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

#why 0 and +1 ???