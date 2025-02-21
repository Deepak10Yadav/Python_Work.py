'''Array and list works similarly but the basic difference is that in list we can store data of different types but in Arrays The Datatype of the data must be same
Arrays Don't have fixed size which leads that we can increase the elements as many as we want''' 
#to use arrays we need to import it.


# there are three ways from which we can import arrays
from array import * # 1 method 
# import array # 2 method
# import array as arr # 3 method

# here we need to mention what is the datatype that will hold.
# # syntax:= variable_Name = array('datatype icon' , [Values(or)Datas]) 

a = array('i',[1, 2, 3, 4])
b = array(a.typecode, (e for e in a)) # if we want the same values of the other array we use this.
print(a.buffer_info()) # .buffer_info() will give size and address of an array and it is a function of array there are multiple functions in array.
a.append(8)
a.reverse() # it will reverse the array
for i in range(len(a)):
    print(a[i])

# Array Values Form User
arr = array('i',[])

n = int(input("Enter The Length Of Array : "))

for i in range(n):
    x = int(input("Enter The Value : "))
    arr.append(x)

print(arr)

#method  1
val1= int(input("Enter The Value To Search : ")) # to searcch elements form the array.
k = 0
for e in arr:
    if e==val1:
        print(k)
        break
    k+=1
# method 2
print(arr.index(val1))