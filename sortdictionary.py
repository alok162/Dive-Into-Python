mydict = {'carl':40, 'alan':2, 'bob':10, 'danny':3}  
print(sorted(mydict.items(), key=lambda x : x[0]))

# It will print [('alan', 2), ('bob', 10), ('carl', 40), ('danny', 3)]


# mydict = {'carl':40, 'alan':2, 'bob':10, 'danny':3}  
# print(sorted(mydict.items(), key=lambda x : x[1]))

# it will print [('alan', 2), ('danny', 3), ('bob', 10), ('carl', 40)]