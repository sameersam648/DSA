def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


#it was just about printing the fibonacci one by one rather then using for loop