arr = [1,2,2,3,4,4,5]
# just added from the question 

seen = set() #created a set to add all the elements of the list
result = [] #only the not repeatec elements are shift to here from seen set

for num in arr:
    if num not in seen:
        seen.add(num) #all the elements are added to seen set
        result.append(num) # only the non repeated elements are added to result list

print(result)