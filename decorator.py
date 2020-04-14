def my_deco(func):
    def inner(s):
        return s+' INR'
    return inner

@my_deco
def temp(s):
    return s

print(temp('500'))
