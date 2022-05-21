from abc import ABCMeta, abstractstaticmethod

## This design pattern (the singleton pattern) can only be instantiated
## once.

## Interface
class IPerson(metaclass=ABCMeta):
    def print_data():
        """ Implemented in singleton class """

## Singleton class
class PersonSingleton(IPerson):
    """ Singleton Class can only be instantiated once """

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Person Name", 25)
        return PersonSingleton.__instance

    def __init__(self, name, age):

        if PersonSingleton.__instance != None:
            raise Exception("You cant do that more than once bud!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    def print_data(self):
        print(f"My name is {self.name} and I am currently {self.age} years old!")

## Works
p1 = PersonSingleton("Mike", 40)
print(p1.print_data())


## Fails
p2 = PersonSingleton("Jim", 55)
print(p2.print_data())