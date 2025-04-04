#  Single Inheritance
'''class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

obj = Child()
obj.display()  #
obj.show()     
'''

#  Multiple Inheritance
'''class Parent1:
    def method1(self):
        print("This is Parent1")

class Parent2:
    def method2(self):
        print("This is Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("This is Child class")

obj = Child()
obj.method1()
obj.method2()
obj.method3()
'''

# Multilevel Inheritance
'''
class GrandParent:
    def grand_method(self):
        print("This is the Grandparent class")

class Parent(GrandParent):
    def parent_method(self):
        print("This is the Parent class")

class Child(Parent):
    def child_method(self):
        print("This is the Child class")

obj = Child()
obj.grand_method()
obj.parent_method()
obj.child_method()'''

# Hierarchical Inheritance
'''class Parent:
    def parent_method(self):
        print("This is the Parent class")

class Child1(Parent):
    def child1_method(self):
        print("This is Child1 class")

class Child2(Parent):
    def child2_method(self):
        print("This is Child2 class")

obj1 = Child1()
obj1.parent_method()
obj1.child1_method()

obj2 = Child2()
obj2.parent_method()
obj2.child2_method()'''

#  Hybrid Inheritance
'''
class Base:
    def base_method(self):
        print("Base class method")

class Derived1(Base):
    def derived1_method(self):
        print("Derived1 class method")

class Derived2(Base):
    def derived2_method(self):
        print("Derived2 class method")

class Derived3(Derived1, Derived2):
    def derived3_method(self):
        print("Derived3 class method")

obj = Derived3()
obj.base_method()
obj.derived1_method()
obj.derived2_method()
obj.derived3_method()
'''

#  Overloading and Overriding

'''class Example:
    def add(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Sum: {a + b}")
        elif a is not None:
            print(f"Single argument: {a}")
        else:
            print("No arguments")

obj = Example()
obj.add(5, 10)
obj.add(5)
obj.add()
'''

'''
class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class (Overridden method)")

obj = Child()
obj.show()
'''

'''
#  Encapsulation with All Access Modifiers
# Public 
class Example:
    def __init__(self):
        self.public_var = "public"

obj = Example()
print(obj.public_var) 

# Protected 
class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

obj = Child()
obj.display()  
obj.show()    

# Private
class Demo:
    def __init__(self):
        self.__private_var = "I am a private variable"

    def show(self):
        print("Accessing private variable:", self.__private_var)

obj = Demo()
obj.show()
'''

# Polymorphism
'''class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak()) 


class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Circle(5)]
for shape in shapes:
    print("Area:", shape.area())  '''
