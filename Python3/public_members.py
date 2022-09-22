class Test:
    
    def __init__(self) -> None:
        self.x = 10 # public variable
    
    def m1(self): # public method
        print('public method')
    
    def m2(self):
        print(self.x)
        self.m1 # public members within the class , can be accessed

# public members outside class can be accessible
test = Test()
print(test.x)
test.m1()
