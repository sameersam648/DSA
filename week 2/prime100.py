def is_prime(n):
    if n <= 0:
        return False
    for i in range(2,int(n**2 + 1)):
        if n % i  == 0:
            return True
    return False

print(is_prime(2))

def prime_generator(limit):
    for num in range(2,limit+1):
        yield num

for prime in prime_generator(100):
    print(prime,end =" ")


#done!!!, it was intresting