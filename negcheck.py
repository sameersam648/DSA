def negcheck(num):
    if num < 0:
        raise ValueError("Input cannot be negative")
    return num

print(negcheck(10))
negcheck(-10)
