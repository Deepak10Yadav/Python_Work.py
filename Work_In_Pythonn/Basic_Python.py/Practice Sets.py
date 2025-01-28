# Chapter  - 9 
# Practice Set 

# Q.2 
# import random

# def game ():
#     print("You Are Playing The Game..!!!")
#     score = random.randint(1, 62)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore=0
    
#     print(f"Your Score : {score}")
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()

# Q.3 --------------------------------------------------------------------------------------------------------------------------------

# def generateTable(n):
#     table=""
#     for i in range(1,11):
#         table += f"{n} X {i} = {i*n}\n"
    
#     with open(f"table/table_{n}","w") as f:
#         f.write(table)


# for i in range(2,21):
#     generateTable(i)


# <<<<<<<<<<<<<<<<<=======================>>>>>>>>>>>>>>>>>>>>>
#Chapter 11 Practice Set

# class TwoDvector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"the vector is {self.i}i +{self.j}j ")

# class ThreeDVector(TwoDvector):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k= k

#     def show(self):
#             print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

# a  = TwoDvector(1,2)
# a.show()
# b = ThreeDVector(1,2,3)
# b.show()

# --------------------------------->>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<------------------------------------
# practice set 12

# Q.1
# try:

#      with open("1.txt","r"):
#        print(f.read())
# except Exception as e:
#     print(e)

# try:

#      with open("2.txt","r"):
#        print(f.read())
# except Exception as e:
#     print(e)

# try:

#      with open("3.txt","r"):
#        print(f.read())
# except Exception as e:
#     print(e)

# @Q.2
# l =[1, 2, 3, 4, 5, 6 , 7, 8]
# for i,item  in enumerate(l):
#     if i == 2  or i == 4 or i == 6:
#         print(item)

# Q.3
# table = int(input("Enter a Number : "))
# m = [table*i for i in range(1,11)]
# print(m)

# Q.4 
try:
    a = int(input("Enter The Number"))
    b = int(input("Enter The Number"))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinte Number") 
