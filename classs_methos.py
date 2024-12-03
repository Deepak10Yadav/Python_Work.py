# class employee:
#     a = 1
#     def show(self):
#         print(f"The Class Attribute of a is {self.a}")
# e = employee()
# e.a = 45

# e.show()

# Output of this cide will be 45.

# @classmethod

class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The Class Attribute of a is {cls.a}") # it will 45 not the class value 1. becz in line 8 we had its value as we know the 
        #it will take the object value if we had given so if we want to access the class value we have to use the @classmethod decorator. 

e = employee()
e.a = 45

e.show()

#output of this code 1. as we used @classmethod to access the class value of a.