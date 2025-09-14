#first make a list of numbers 
numbers = [10, 20, 30, 50,60]

#open file to write 
with open("numbers.txt", "w") as file:
    #run a for loop to add number 1 by 1
    for num in numbers:
        #send number to numbers.txt
        file.write(str(num) + "\n")
    
