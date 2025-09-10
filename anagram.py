#sorted technique
'''
def are_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagram("listen", "silent"))'''

## DSA approach

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) +1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        freq[ch] = freq.get(ch, 0) +1
    return True


print(anagram("listen", "silent"))


# this was tough, yet i did it , didn't give up!!!!!


#and with this the first week of python basic's fo DSA is done !
#new achievement unlocked.