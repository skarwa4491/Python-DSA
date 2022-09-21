def decorate(func):
    def inner():
        print("i am decorating this")
        func()
    return inner

@decorate
def display():
    print('hello world')

display()