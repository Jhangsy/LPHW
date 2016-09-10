## Animal is-a object. "object" is a class of python you inherit when you make a new class.
class Animal(object):
    pass

##Dog is-a Animal has-a __init__ takes self and name parameters.
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name of some kind
        self.name =name
##Cat is-a Animal has-a __init__ takes self and name parameters.
class Cat(Animal):

    def __init__(self, name):
        ##cat has-a name
        self.name = name

##Person is-a object has-a __init__ takes self and name parameters.
class Person(object):

    def __init__(self, name):
        ##Person has a name.
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##call __init__ from superclass
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

##Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

##Hlibut is-a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog.
rover = Dog("Rover")

##Satan is-a Cat
satan = Cat("Satan")

##Mary is a Person.
mary = Person("Mary")

##Marry has-a pet named satan is-a Cat
mary.pet = satan

## Frank is a Employee has-a Salary
frank = Employee("Frank", 120000)

##frank has-a pet named rover is-a Dog.
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a  Hlibut()
harry = Halibut()
