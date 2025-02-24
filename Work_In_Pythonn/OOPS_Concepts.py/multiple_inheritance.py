class Employee:  #ye ek main class hai.(Parent Class)
    company = "ICT" 
    name = "Deepak"
    def show(self):
        print(f"The Name Of  Employee is {self.name} and the Company is {self.company}")

class Code:  #ye bhi ek parent class hai 
    language = "python"
    def lanshow(self):
        print(f"The Language In Which He Is Good Is {self.language}")

class Programer(Employee, Code):   #jab koi bhi do  parent class ki property ek inhertance class me aajaye tab haam usse multiple inheritance bolteyy
    company = "ICT G1"
    def ShowL(self):
        print(f"The Name Of  Employee is {self.name} and the Company is {self.company}")

a = Employee()
b = Programer()

b.show()
b.lanshow()
b.ShowL()

# print(a.company, b.company,b.name)