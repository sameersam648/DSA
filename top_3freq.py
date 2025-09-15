from collections import Counter

def top_Kcounter(nums, k):
    freq = Counter(nums)
    return freq.most_common(k)

nums = [1,2,3,4,2,4,32,5,34,234,2,3,4,43,2,3]
print(top_Kcounter(nums,3))

#done "!