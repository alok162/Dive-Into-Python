def my_deco(obj):
    def inner_func():
        print 'decorator function executed',obj
        return obj
    return inner_func

@my_deco
def display():
    print  'display function executed'

display()