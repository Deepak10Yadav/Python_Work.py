# # Chapter  - 9 
# # Practice Set 

# # Q.2 
# # import random

# # def game ():
# #     print("You Are Playing The Game..!!!")
# #     score = random.randint(1, 62)
# #     with open("hiscore.txt") as f:
# #         hiscore = f.read()
# #         if(hiscore != ""):
# #             hiscore = int(hiscore)
# #         else:
# #             hiscore=0
    
# #     print(f"Your Score : {score}")
# #     if(score>hiscore):
# #         with open("hiscore.txt", "w") as f:
# #             f.write(str(score))

# #     return score

# # game()

# # Q.3 --------------------------------------------------------------------------------------------------------------------------------

# # def generateTable(n):
# #     table=""
# #     for i in range(1,11):
# #         table += f"{n} X {i} = {i*n}\n"
    
# #     with open(f"table/table_{n}","w") as f:
# #         f.write(table)


# # for i in range(2,21):
# #     generateTable(i)


# # <<<<<<<<<<<<<<<<<=======================>>>>>>>>>>>>>>>>>>>>>
# #Chapter 11 Practice Set

# # class TwoDvector:
# #     def __init__(self,i,j):
# #         self.i = i
# #         self.j = j

# #     def show(self):
# #         print(f"the vector is {self.i}i +{self.j}j ")

# # class ThreeDVector(TwoDvector):
# #     def __init__(self, i, j,k):
# #         super().__init__(i, j)
# #         self.k= k

# #     def show(self):
# #             print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

# # a  = TwoDvector(1,2)
# # a.show()
# # b = ThreeDVector(1,2,3)
# # b.show()

# # --------------------------------->>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<------------------------------------
# # practice set 12

# # Q.1
# # try:

# #      with open("1.txt","r"):
# #        print(f.read())
# # except Exception as e:
# #     print(e)

# # try:

# #      with open("2.txt","r"):
# #        print(f.read())
# # except Exception as e:
# #     print(e)

# # try:

# #      with open("3.txt","r"):
# #        print(f.read())
# # except Exception as e:
# #     print(e)

# # @Q.2
# # l =[1, 2, 3, 4, 5, 6 , 7, 8]
# # for i,item  in enumerate(l):
# #     if i == 2  or i == 4 or i == 6:
# #         print(item)

# # Q.3
# # table = int(input("Enter a Number : "))
# # m = [table*i for i in range(1,11)]
# # print(m)

# # Q.4 
# # try:
# #     a = int(input("Enter The Number"))
# #     b = int(input("Enter The Number"))
# #     print(a/b)
# # except ZeroDivisionError as z:
# #     print("Infinte Number") 


# # Linked_List
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Linkedlist:
#     def  __init__(self):
#         self.head=None
#     def traversal(self):
#         if self.head is None:
#             print("Empty")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data,end="->")
#                 a = a.next
#     def insert_at_begg(self,data):
#         print()
#         b= Node(data)
#         b.next=self.head
#         self.head = b

#     def insert_at_end(self,data):
#         print()
#         c= Node(data)
#         f = self.head
#         while f.next is not None:
#             f=f.next
#         f.next = c

#     def insert_in_between(self, data, position):
#         print()
#         M1= Node(data) 
#         Fix = self.head
#         for i in range (1,position-1):
#             Fix =Fix.next
#         M1.next=Fix.next
#         Fix.next = M1
#     def delete_at_beg(self):
#         print()
#         rr = self.head
#         self.head = rr.next
#         rr.next = None

#     def delete_at_end(self):
#         print()
#         prev = self.head
#         r1 = self.head.next
#         while r1.next is not None:
#             r1 = r1.next
#             prev  = prev.next
#         prev.next = None
#     def delete_in_bet(self,position):
#         print()
#         prev = self.head
#         a = self.head.next
#         for i in range (1,position - 1):
#             a=a.next
#             prev = prev.next
#         prev.next=a.next
#         a.next= None


# z1 = Linkedlist()
# n1 = Node(1)
# z1.head = n1
# n2 = Node(2)
# n1.next = n2
# n3 = Node(3)
# n2.next = n3
# n4 = Node(4)
# n3.next= n4
# n5 = Node(5)
# n4.next = n5
# n6 = Node(6)
# n5.next=n6
# z1.insert_at_begg(9)
# z1.traversal()
# z1.insert_at_end(8)
# z1.traversal()
# z1.insert_in_between(67,4)
# z1.traversal()
# z1.delete_at_beg()
# z1.traversal()
# z1.delete_at_end()
# z1.traversal()
# z1.delete_in_bet(2)
# z1.traversal()

# import numpy as np
# matrix1= np.array([[1,2,3],
#                    [6,9,3],
#                    [3,2,1],
#                    [6,7,8],
#                    [3,6,4]])

# matrix2 = np.array([[2,3],
#                     [4,1],
#                     [6,7]])

# aa1 = np.dot(matrix1,matrix2)
# print(aa1)



# print(sum(range(5),-1))
# print(sum(range(5),-2))

# from numpy import *
# print(sum(range(5),-1))
# print(sum(range(5)))

# '''python
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z
# '''
# import numpy  as np
# Z = np.array([]) 


# np.array(0) / np.array(0)

# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)



# import numpy as np
# arr = np.array([1.2, -1.2, 2.5, -2.5, 0.0])
# rounded = np.where(arr > 0, np.ceil(arr), np.floor(arr)) 
#np.ceil() rounds up toward positive infinity.
#np.floor() rounds down toward negative infinity.
# np.where() applies the correct function based on the sign of each number.



# import numpy as np
# a = np.array([1,2,3,4,5])
# b = np.array([6,5,8,9,10])

# common = np.intersect1d(a,b) # to find common value  of any array we use np.intersect1d it finds  the intersection value of the arrays.
# print(common)

# 33. How to get the dates of yesterday, today and tomorrow?
# Answer:
# import numpy as np
# from datetime import date,timedelta

# today = date.day
# print(today)

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

# np.sqrt(-1) == np.emath.sqrt(-1)

# 37. Create a 5x5 matrix with row values ranging from 0 to 4

# import numpy as np
# matrix = np.array(([0,2,3,4,5],
#                    [1,6,4,3,7],
#                    [2,7,8,4,6],
#                    [3,8,0,4,2],
#                    [4,7,8,5,9]))
# print(matrix)

#38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
# import numpy as np
# s = int(input("Enter The Number:"))
# def generator():
#     a= np.random.random(s)
#     print(a)

# b = np.array([(generator)])
# print(b)
# generator()


import numpy as np

# Create 10 evenly spaced values between 0 and 1, excluding both endpoints
# vector = np.linspace(0, 1, 12)[1:-1]
# print(vector)

# method - 2
# vector1 = np.random.uniform(low=0.1,high=0.9,size=10)
# print(vector1)

#### 40. Create a random vector of size 10 and sort it (★★☆)

# vector = np.random.random(10)
# vector.sort()
# print(vector)

#### 42. Consider two random arrays A and B, check if they are equal (★★☆)

# a = np.random.random((3))
# b = np.random.random((3))
# print(a)
# print(b)
# print(a==b)

#### 43. Make an array immutable (read-only) (★★☆)

# arr1 = np.ones([6])
# arr1.setflags(write=False) # it will run untill any operations makes an error.after error it will give you ValueError.
# arr1[2] = 3 # here we are trying to change the value of array := arr1  aat position 2 and it is giving the error becz now the array is immutabe.
# print(arr1)

#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

# arr2 = np.random.random((10,2))
# print("array1:",arr2)
# arr3 = np.random.random((10,2))
# print("array2:",arr3)
# # r = √(x² + y²) formula to convert cartesian to polar.
# square1 = np.square(arr2,arr3) #(x² + y²)
# print("sqaure:",square1)
# formula = np.sqrt(square1) #√(x² + y²)
# print("polar:",formula)


#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

# vector=np.random.random(10)
# vector[vector.argmax()]=0
# print(vector)


# 49. How to print all the values of an array? (★★☆)
# import sys
# array1 = np.ones([4,5])
# print(array1)

#### 50. How to find the closest value (to a given scalar) in a vector?

# vec = np.array(([0.1,0.5,0.7,0.8,0.4,0.2]))
# scl = 1.0
# a = np.abs(vec - scl).argmin()
# vec1=vec[a]
# print(vec1)

#### 51.Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
# import matplotlib.pyplot as plt
# x = np.array([1,2,3])
# y = np.array([4,5,7])
# color = ['red','green','blue']
# plt.scatter(x,y,c=color)
# plt.show()
# print(x)
# print(y)




# 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
# vector  = np.random.random((100,2))
# diff = np.diff(vector)
# print(diff)

# 53. How to convert a float (32 bits) array into an integer (32 bits) array in place?
# array1 = np.array([1.6,2.5,3.1,4.9])
# m1 = (list(map(int,array1)))  # method - 1
## m2 = [int(x) for x in array1] #method - 2 
# print(m1)
# print(m2)



# 54. How to read the following file? (★★☆)
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
from io import StringIO # its create a string to file. # Convert string to file-like objects.
csv_data = StringIO("""
1,2,3,4,5
6,, ,7,8
,,9,10,11
""")
data = np.genfromtxt(csv_data,delimiter=',', dtype=float)
print(data)
