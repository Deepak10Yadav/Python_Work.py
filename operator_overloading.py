class Number:
    def __init__(self, n ):
        self.n = n
    def __add__(self,num): # here we need to define every  operator for python if i don't write this line of code (line 4 and line 5) then it will give an 
        # error we have define every operator before using it.
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n+m)

#there are multiple operators like: 
#p1+p2  -----------> # p1.__add__(p2)
#p1-p2  -----------> # p1.__sub__(p2)
#p1*p2  -----------> # p1.__mul__(p2)
#p1/p2  -----------> # p1.__truediv__(p2)
#p1//p2 -----------> # p1.__floordiv__(p2)

# __str__() # used to set what gets displayed upon calling str(obj) 
# __len__() # used to set what gets displayed upon calling.__len__() or len(obj)
