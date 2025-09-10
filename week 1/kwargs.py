#**kwargs take the key and value both of any numbers

def key_values(**kwargs):
    for key in kwargs: #it takes the keys
        value = kwargs[key] # then this takes the values 
        print(key, " : ", value) #this prints both key and value 


key_values(name = "sameer", age = "22", city = "Bangalore")


#i did it in first try