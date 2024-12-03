class Employee:  #ye ek main class hai.(Parent Class)
    company = "ICT" 
    def show(self):
        print(f"The Name Of  Employee is {self.name} and the salary is {self.salary}")

# class Programer:
#     company = "ICT G1"    #Agar merko kuch bhi change krna hai tho mmujhe saab ne change krna padega kyuki saab same rakhna hai aur agar 
# me aaise banaunga tho  bhut time legega tho isliye haam ek inhertance class banate hai usmai agar hamne kuch bhi change kiya main class me tho 
# inheritance class me khud hee change hojata hai.
#     def show(self):
#         print(f"The Name Of  Employee is {self.name} and the salary is {self.salary}")

#     def show(self):
#         print(f"The Name Of  Employee is {self.name} and the salary is {self.salary}")

class Programer(Employee):   # Ye Ek Inheitance class hai(Derived Or Child Class)
    company = "ICT G1"
    def ShowL(self):
        print(f"The Name Of  Employee is {self.name} and the salary is {self.salary}")

a = Employee()
b = Programer()

print(a.company, b.company)