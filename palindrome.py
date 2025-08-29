def is_palendrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palendrome("Racecar"))
print(is_palendrome("madam"))
print(is_palendrome("sAMEER"))


