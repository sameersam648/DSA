#new liberatly called itertools, that is used to find possibl ecombinations in a list 
from itertools import combinations

arr = [1,2,3,4,5]
pair = list(combinations(arr,2))
print(pair)