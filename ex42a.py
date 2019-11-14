## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    # pass
    def __init__(self):
        pass

    def hello_world(self, name):
        print(f"hello world, {name}, I just said it because this fucking programming learner told me so, so fuck you")

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def bark(self):
        print("FUCKING AAAAAAAs")

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def say_hi(self):
        print("Hi, I am a human")

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

class wolve(Animal):

    def __init__(self, name):
        self.name = name

    def say_something(self):
        print("AHHHH WOOHHHH")

class wolverine(wolve, Person):

    def __init__(self):
        pass

    def clawout(self):
        print("I'm inevitable")

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

# rover.bark()
# rover.hello_world("Vivi")

logan = wolverine()
logan.say_hi()
logan.say_something()
logan.clawout()
