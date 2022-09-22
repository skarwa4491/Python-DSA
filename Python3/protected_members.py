class Parent:
    '''
        protected data members can be accessed only from within the class
        or from child classes
        
        protected members can be declared with _ prefixed
        
        protected in python is just a convention , this can be accessed from
        outside class as errors are not programmed at language level
    '''
    def __init__(self) -> None:
        self._x = 10
        
    def m1(self):
        print(self._x) # acceptable

class Child(Parent):
    
    def m1(self):
        print(self._x) # acceptable
    
    
    