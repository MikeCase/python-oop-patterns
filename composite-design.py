from abc import ABCMeta, abstractmethod, abstractstaticmethod

# Composite Method is a Structural Design Pattern which describes a group of objects that is treated the same way as a single instance of the same type of the objects.
# The purpose of the Composite Method is to Compose objects into Tree type structures to represent the whole-partial hierarchies.
# One of the main advantages of using the Composite Method is that first, it allows you to compose the objects into the Tree Structure and then work with these structures
# as an individual object or an entity.

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """

    @abstractstaticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees


    def print_department(self):
        print("Parent department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()

        print(f"Total # of employees: {self.employees}")


dept1 = Development(200)
dept2 = Accounting(175)

pdept = ParentDepartment(30)
pdept.add(dept1)
pdept.add(dept2)

pdept.print_department()