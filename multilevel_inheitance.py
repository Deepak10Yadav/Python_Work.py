class Employee:
    a= 1
class programer(Employee):
    b=2
class manager(programer):
    c=3

o = Employee()
print(o.a)
# print(o.b) #this will  show an error as there is no b attribute in employee class

v=programer()
print(v.a,v.b) #here it will print a and b both becz we had created progamer class with the help of employee class so the property of 
#employee class will be inherited to programer class

m=manager()
print(m.a,m.b,m.c) # here it will print everything
