def fibonacci():
    a,b = 0,1
    #it uses while loop that is why it is infinite , it runs until the condition is met 
    while True:
        yield a
        a,b = b, a+b

fib = fibonacci()

for _ in range(100):
    print(next(fib), end=" ")