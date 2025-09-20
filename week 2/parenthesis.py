def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("((()))"))
print(is_balanced("((((())))"))

#i did ittt!!!! , 
# i am getting a hold of it.