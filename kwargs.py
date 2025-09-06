#**kwargs take the key and value both of any numbers

def key_values(**kwargs):
    for key in kwargs:
        value = kwargs[key]
        print(key, " : ", value)


key_values(name = "sameer", age = "22", city = "Bangalore")


#i did it in first try