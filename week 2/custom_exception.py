# to create a custom exception condition, like ValueError .

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative Number is not accepted{value}")

#the funciton for calsulating factorial of a number
def factorial(n):
    if n < 0:
        raise NegativeNumberError(n)
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
    
try:
    print(factorial(5))
    print(factorial(-1))



except NegativeNumberError as e:
    print("Cauth an error", e)