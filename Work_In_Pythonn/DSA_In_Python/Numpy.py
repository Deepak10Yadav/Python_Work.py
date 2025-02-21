from numpy import *
# type of creating an array
# 1.array()
num =array([1,2,3,4,5,6])
print(num)

# 2.linespace()
num1 = linspace(0,12,6) #here 0 to 12 will Work as an range and 6 is in how many parts we want to break the range. 
print(num1)

# 3.logspace()
arr1 = logspace(1,40,5) # it will give the values in log.
print('%.2f' %arr1[1]) # to get full values we use % symbol.

# 4.a-range()
arr = arange(1,15,2) # here we had give the range from 1 to 15 but with an skip elements of 2 it will 2 numbers and print next one.
print(arr)

# 5.zeros()
zero0 = zeros(5,int) # 5 = size  
print(zero0)

# 6.ones()
on1 = ones(5,int)  # 5 = size 
print(on1)


# few oprations on array
# we can runn all maths operations here.

arr21 = array([1, 2, 3, 4, 5])
arr22 = array([5, 6, 7, 8, 9])
arr23 = arr21 + 5 
arr33 = arr21 + arr22
# to print all the array in one single array we use concatenate func.
print(concatenate([arr21,arr22]))
print(arr23)
print(sin(arr33))
print(cos(arr33))
print(log(arr33))
print(sqrt(arr33))
print(min(arr33))
print(max(arr33))

# coping the array
a = array([7,6,5,4,3])
# b = a.copy()
b = a.view() # if we use view function then the values will be copied but the address will be changed.
# there are two types of array copy in numpy 
# 1. Shallow Copy
a[2] = 66 # here we had changed the value on index no.2
# in shallow copy it will change the value for both like the one in which we want the change and in one we are coping 
# 2. Deep Copy
# a[1] = 55
# a = a.copy() in line 47 we had use copy fucntion
# to use deep copy we use function called copy.
print(a)
print(b)

print(id(a)) # used to check id/address of the element.
print(id(b)) # used to check id/address of the element.

