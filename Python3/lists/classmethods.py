from datetime import date


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def instance_method(self):
        self.print_this(self.name , self.age)

    @classmethod
    def from_birth(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def print_this(name,age):
        print('my name is {name} and my age is {age}'.format(
            name=name, age=age))


p1 = Person('swapnil', 21)
p2 = Person.from_birth('Pooja', 1993)
p1.instance_method()
p2.instance_method()

print(p1.age, p2.age)
