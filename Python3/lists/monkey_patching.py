from contextlib import contextmanager


class A:
    def display(self):
        print('swapnil')

class B:
    def display(self):
        print('karwa')
        

@contextmanager
def mock_method():
    original = A.display
    A.display = B.display
    yield
    A.display=original
    
with mock_method:
    a = A()
    a.display()