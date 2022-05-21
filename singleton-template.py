class SingletonPattern:

    __instance = None

    @staticmethod
    def get_instance():
        if SingletonPattern.__instance == None:
            SingletonPattern(*args)
        return SingletonPattern.__instance

    def __init__(self, *args):
        if SingletonPattern.__instance != None:
            raise Exception("Can only initialize once.")
        else:
            self.args = args
            SingletonPattern.__instance = self

    def print_args(self):
        for arg in self.args:
            print(arg)



## Works
data = SingletonPattern("Mike", 50, 5.0, ['this','is','a','list'])
print(data.print_args())


## Fails
data1 = SingletonPattern("John", 25, 19.0, {"Type":"Dictionary"})
print(data1.print_args())