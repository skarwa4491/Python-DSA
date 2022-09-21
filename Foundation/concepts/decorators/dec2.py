def decorator(func):
    def inner(a,b): # should contain same number of arguments of original function
        print('addition is {result}'.format(result = func(a,b)))
    return inner

@decorator
def add(a,b):
    return str(a+b)

add(20,30)        