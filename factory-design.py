from abc import ABCMeta, abstractmethod, abstractstaticmethod


## Factory pattern can be used if you need to have different
## types of an entity.
class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):

    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"My name is {self.name} and I am a student.")

class Teacher(IPerson):

    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"My name is {self.name} and I am a teacher.")


class PersonFactory:


    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student("Mike")
        if person_type == "Teacher":
            return Teacher("Jim")
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    choice = input("Would you like to create a student, or a teacher? [Student/Teacher]: ")
    person = PersonFactory.build_person(choice)
    person.person_method()
