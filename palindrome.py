'''def is_palendrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palendrome("Racecar"))
print(is_palendrome("madam"))
print(is_palendrome("sAMEER"))
'''

def is_palindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("madam"))
print(is_palindrome("sameer"))

