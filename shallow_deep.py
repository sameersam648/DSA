import copy

original = [[1,2], [3,4]]

shallow = copy.copy(original)

deep = copy.deepcopy(original)

original[0][0] = '99'

print("original:", original)
print("shallow:", shallow)
print("deep :", deep)

''' the only thing i understood from this is the box is changing 
but the values inside is changing'''