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
# try:
#     a = int(input("Enter The Number"))
#     b = int(input("Enter The Number"))
#     print(a/b)
# except ZeroDivisionError as z:
#     print("Infinte Number") 


# Linked_List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def  __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("Empty")
        else:
            a = self.head
            while a is not None:
                print(a.data,end="->")
                a = a.next
    def insert_at_begg(self,data):
        print()
        b= Node(data)
        b.next=self.head
        self.head = b

    def insert_at_end(self,data):
        print()
        c= Node(data)
        f = self.head
        while f.next is not None:
            f=f.next
        f.next = c

    def insert_in_between(self, data, position):
        print()
        M1= Node(data) 
        Fix = self.head
        for i in range (1,position-1):
            Fix =Fix.next
        M1.next=Fix.next
        Fix.next = M1
    def delete_at_beg(self):
        print()
        rr = self.head
        self.head = rr.next
        rr.next = None

    def delete_at_end(self):
        print()
        prev = self.head
        r1 = self.head.next
        while r1.next is not None:
            r1 = r1.next
            prev  = prev.next
        prev.next = None
    def delete_in_bet(self,position):
        print()
        prev = self.head
        a = self.head.next
        for i in range (1,position - 1):
            a=a.next
            prev = prev.next
        prev.next=a.next
        a.next= None


z1 = Linkedlist()
n1 = Node(1)
z1.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next= n4
n5 = Node(5)
n4.next = n5
n6 = Node(6)
n5.next=n6
z1.insert_at_begg(9)
z1.traversal()
z1.insert_at_end(8)
z1.traversal()
z1.insert_in_between(67,4)
z1.traversal()
z1.delete_at_beg()
z1.traversal()
z1.delete_at_end()
z1.traversal()
z1.delete_in_bet(2)
z1.traversal()