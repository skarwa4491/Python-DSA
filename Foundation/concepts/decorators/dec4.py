from xml.dom.expatbuilder import FilterVisibilityController


def decorate(func):
    def inner(a,b):
        try:
            func(a,b)
        except ZeroDivisionError:
            print('zero division error')
    return inner

@decorate
def divide(a,b):
    print(a//b)

divide(5,0)