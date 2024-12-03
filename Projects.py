#SNAKE , WATER , GUN (GAME)

# '''
# snake = 1
# water = 2 
# gun = 0
# '''
# computer = input("Enter Computer Choice : ")  #to  compare any values like here the datatype should be same 
# # Like here i had taken input in the form of string.
# youstr = input("Enter Your Choice : ")
# youDict = {"s":1 ,"w":2 , "g":0}
# you=youDict[youstr]

# if(computer == you):
#     print("Draw")

# else:
#     print("Else")
#     print(str(you))
#     if(computer == 1 and you == 2):    # and i am comparing it here while comparing the input datatype is string and here in condition statement the datatype is integer so to
#      #solve this we can do 2 thing we Should change the datatype of input computer like:- int(input("Enter The Choice Of User : "))   2nd method is we should change it in every 
#      #if and elif statement like :- if(computer == "1" and you == 2) #here we had writen 1 in semicolon due to which here the datatype is converted from integer to string now
#      # it will be compared.  
#      print("You Win!!")

#     elif(computer == 0 and you == 1):
#      print("You Lose!!")

#     elif(computer  == 0 and you == 2):
#      print("You Win!!")

#     elif(computer == 2 and you == 0):
#      print("You Win!!!")

#     elif(computer == 2 and you == 1):
#       print("You Lose")
#     else:
#      print("Default")


# Correct Code :- 

# Method 1: -

# SNAKE , WATER , GUN (GAME)

# '''
# snake = 1
# water = 2 
# gun = 0
# '''
# computer = int(input("Enter Computer Choice : "))  #to  compare any values like here the datatype should be same 
# youstr = input("Enter Your Choice : ")
# youDict = {"s":1 ,"w":2 , "g":0}
# you=youDict[youstr]

# if(computer == you):
#     print("Draw")

# else:
#     print("Else")
#     print(str(you))
#     if(computer == 1 and you == 2):
#      print("You Win!!")

#     elif(computer == 0 and you == 1):
#      print("You Lose!!")

#     elif(computer  == 0 and you == 2):
#      print("You Win!!")

#     elif(computer == 2 and you == 0):
#      print("You Win!!!")

#     elif(computer == 2 and you == 1):
#       print("You Lose")
#     else:
#      print("Default")

# Method 2:-

#SNAKE , WATER , GUN (GAME)

# '''
# snake = 1
# water = 2 
# gun = 0
# '''
# computer = input("Enter Computer Choice : ") #to  compare any values like here the datatype should be same 
# youstr = input("Enter Your Choice : ")
# youDict = {"s":1 ,"w":2 , "g":0}
# you=youDict[youstr]

# if(computer == you):
#     print("Draw")

# else:
#     print("Else")
#     print(str(you))
#     if(computer == "s" and you == "w"):
#      print("You Win!!")

#     elif(computer == "g" and you == "s"):    #Ye Bhi Wrong Hai Chacha Ko Puchna hai.
#      print("You Lose!!")

#     elif(computer  == "g" and you == "w"):
#      print("You Win!!")

#     elif(computer == "w" and you == "g"):
#      print("You Win!!!")

#     elif(computer == "w" and you == "s"):
#       print("You Lose")
#     else:
#      print("Default")

# if(computer == "s" and you == "w"):
#   print("You Win!!")

# ---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<--------------------------
#project 2

import random
n = random.randint(1,100)
a = 0
Guesses = 0
while(a!= n):
  Guesses += 1
  a = int(input("Guess The Number: "))
  if(a>n):
        print("Enter The Lower Number!! ")
  else:
        print("Enter The Higher Number!! ")

print(f"You Have Guessed The Number {n} In {Guesses} Guesses")



