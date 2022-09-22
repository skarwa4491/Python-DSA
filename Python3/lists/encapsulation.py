class computer:
    __sell_price = 1000
    
    def __init__(self):
        self.__price = 900
        self.non_private = 200
    
    def set_price(self , price):
        self.__price = price # private variables can only be modified inside a class
        self.__sell_price = 600

    def sell(self):
        print(self.__price)
        print(self.non_private)
        print(self.__sell_price)

laptop = computer()
laptop.sell()
print('#'*30)
laptop.__price = 1000 # unable to modify price , as it is private
laptop.non_private = 400 # this can be modified , as it is non private
laptop.__class__.__sell_price = 500
laptop.sell()
print('#'*30)
laptop.set_price(1200)
laptop.sell()