''' magic methods are also known as Dunder Methods this method
startss from doubke underscore and end at doubke underscore
example := __init__'''

# we use this in a class
class Employee:
    # name = "Vipin"
    def __init__(self,name):
        self.name = name
    def __len__(self):  # here we had created an magic method 
        i = 0
        for a in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"The Name Of The Employee Is {self.name}"
    
    def __repr__(self):
        return f"Employee ('{self.name}')"
    def __call__(self):
        print("Heyyy!!! I Am Good")
    
e = Employee("Vipin")
print(str(e))
print(repr(e))
e() # if we want to print the call method part then we use e().
# print(e.name)
# print(len(e))  # and here we had called that magic method if we call this directly without creating an magic method it will give an error 