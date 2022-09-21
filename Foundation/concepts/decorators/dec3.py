def decorate(func):
    def inner(name):
        if name == 'Karwa':
            print('Good Evening {name}'.format(name = name))
        else:
            func(name)
    return inner

@decorate
def wish(name):
    msg = 'Good Morning {name}'.format(name=name)
    print(msg)

wish('Swapnil')
wish('Karwa')