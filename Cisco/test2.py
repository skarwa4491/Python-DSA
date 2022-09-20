class Parent2:
    
    def display():
        print('Parent2 first name')
        
class Parent(Parent2):
    
    def display(self):
        print("parent first_name")
    
    def show(self):
        print("parent last_name")


class Child(Parent):
    def display(self):
        print('Child first_name')


child = Child()
child.display()