class Test:
    '''
         when we try to access , private members from outside class
         we get 'Attribute error' as python changes the name of private data members to 
        _Class_name__member_name # this concept is called name mangeling
    '''
    def __init__(self) -> None:
        self.__x = 10

    def __m1(self):
        print('private memeber')


test = Test()
print(test._Test__x) # accessing x variable
test._Test__m1() # calling private member