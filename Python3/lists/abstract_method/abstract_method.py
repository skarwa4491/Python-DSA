from abc import ABC, abstractmethod

# this is an abstract class -> which is partially implemented classes
# every abstract class is child class of ABC class , from abc module
# oficially there are not interfaces in python, but they can be mimiced
# by declaring a abstract class , wtih all abstract methods
# abstract class can have bith abstract and non abstract methods , in this scenario 
# class is considered as abstaract class
class vehicle(ABC):
    
    @abstractmethod  # this is an abstract method 
    def get_no_of_wheels(self):
        pass

class bike(vehicle):
    
    def get_no_of_wheels(self):
        return 2

bb = bike()
print(bb.get_no_of_wheels())