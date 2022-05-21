from abc import ABCMeta, abstractstaticmethod


## The proxy design pattern can be used if you need to add extra
## functionality before/after a class method (maybe I'm saying that wrong?)
## Maybe I just don't know what the hell I'm talking about :P

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Person(IPerson):

    def person_method(self):
        print("I'm a regular old person..")

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("Added functionality to the Person class")
        self.person.person_method()
        print("End of added functionality")



p1 = Person()
p1.person_method()
p2 = ProxyPerson()
p2.person_method()
