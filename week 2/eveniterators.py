class EvenIterators:
    #first step in using oops concept is to use the __inti__ that is a constructor of the objects
    def __init__ (self, n):
        self.n = n
        self.current = 0

    #and then the second step is it to define the inerator with (__iter__)
    def __iter__ (self):
        return self
  
    
    #then use the __next__ operator to move to the next object or the element
    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 2
            return result
    


        #else raise the stopiteration 
        else:
            raise StopIteration
        
    def __str__(self):
        return result
#print the output
even = EvenIterators(50)

for num in even:
    print(num, end=",")


#in this code i was getting a warning for writing the itertools name as the file name 
#i was getting the output just the thing was i didn't realize that it was the error from the end="", i didn' leave space between " "