def my_deco(obj):
    def inner_func(designation):
        print 'decorator function executed',obj
        return obj
    return inner_func

@my_deco
def display(designation):
    pass

display('developer')