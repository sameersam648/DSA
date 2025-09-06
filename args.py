#add any number of numbers using args funtion

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
    
print(sum(2,2))
print(sum(23,64,123,5,4,36,3))
print(sum(10,90))

#i made a mistake of not removing the indentation for the return statement
#args is used to take input of any number of elements