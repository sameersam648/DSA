'''
def safe_divide(a,b):
    return a/b if b != 0 else None
'''
#using try except method
def safe_devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: division by 0 is not allowed"



print(safe_devide(50,25))
print(safe_devide(100,0))
