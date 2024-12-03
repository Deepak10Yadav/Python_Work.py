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

class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i +{self.j}j ")

class ThreeDVector(TwoDvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k= k

    def show(self):
            print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a  = TwoDvector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()