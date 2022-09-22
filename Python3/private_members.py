class Test:
    '''
        any data member prefixed with __ is considered as private
        private members can't be accessed from outside a class
        
        when we try to access , private members from outside class
        we get 'Attribute error' as python changes the name of private data members to 
        _Class_name__member # this concept is called name mangeling
    '''
    def __init__(self) -> None:
        self.__x = 10 # private variable
    
    def __m1(self):
        print('private member') # private member 
    
    def m1(self):
        print(self.__x)
        self.__m1() # accessing private member within a class
        
    def m2(self):
        return self.__m1

test = Test()
# print(test.__x) # error here as accessing private member
private = test.m2() # error here as accessing private member
private()