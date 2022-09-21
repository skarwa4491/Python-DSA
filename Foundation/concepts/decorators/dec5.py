# call same function with and without decorator

def decorate(func):
    def inner(name):
        print('with decorated')
    return inner

def display(name):
    print('without decorated')

display('swapnil')
decorated_func = decorate(display)
decorated_func()