class Employee:  # Class Name = Employee
  # name = "Deepak"
  Course = "PowerBI"
  Salary = 1200000

# If We  Creat An  Constructor Then We Don't Have TO Call It Becz It Call's It Self Automatically.
  def __init__(self,name,Salary,Course): # The Methods Which Start From Underscore Are Known As ------>>>>> Dunder Methods. 
    # All Methods Of This Type(Dunder) Can Call It Itself.
    self.name = name
    self.Salary = Salary
    self.Course = Course
    print("This Is An Object")

  
  def getInfo(Self): 
    print(f"The Salaray is {Self.Salary}.\nThe Couse Is {Self.Course}")

  @staticmethod 
  def greet(): 
    print("goodmorning") 

Deepak =  Employee("Deepak","PowerBi",100000)  # Sequence Of Passing An Argument Dose Not Matter...
print(Deepak.name,  Deepak.Course,Deepak.Salary) # we had to mention/pass the things that we Want to print.
# Deepak.Course= "Python"
# Deepak.getInfo()
# Deepak.greet()