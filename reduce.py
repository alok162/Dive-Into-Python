#reduce takes two arguments and naturally gives the result
arr = [1,2,3,4,5]
print reduce(lambda x, y: x+y, arr)

# o/p 15