class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The Class Attribute of a is {cls.a}") # it will 45 not the class value 1. becz in line 8 we had its value as we know the 
        #it will take the object value if we had given so if we want to access the class value we have to use the @classmethod decorator.
    @property
    def name(self):
            return f"{self.fname} {self.lname}"

    @name.setter
    def name (self,value):
            self.fname = value.split(" ")[0] # here the split function will split the user name like it will convert it into a list
            #jaha jaha space hoga utna comma krke vho list banata jayega.
            self.lname = value.split(" ")[1]

e = employee()
e.a = 45

e.name = "Deepak Yadav"
print(e.fname,e.lname)

e.show()