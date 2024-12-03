class Employee:
    def __init__(self):
        print("This Is A Constructor Of Employee ")
    a= 1
class programer(Employee):
    def __init__(self):
        print("This Is A Constructor Of Programer ")
    b=2
class manager(programer):
    def __init__(self):
        super().__init__() #becz of this the constructor of its parent class will be printed as well
        print("This Is A Constructor Of Manager ")
    c=3

# o = Employee()
# print(o.a)


# v=programer()
# print(v.a,v.b) 

m=manager()  # here if we print this then it just print the consructor of this one only but if we want to
#print the cconstuctor of its parent class then we use (superkey)
print(m.a,m.b,m.c) 
