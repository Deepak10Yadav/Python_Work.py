# a= (input("Enter The Number 1: "))
# b= input("Enter The Number 2: ")
# C= input("Enter The Number 3: ")
# t=type(b)
# d=type(C)
# x=type(a)
# print(t,d,x )


# print("The Sum Of Number Entered By User Is: ", a+b,a*b)

# a=int(input("Enter The Number 1: "))
# b=int(input("Enter The Number 2: "))
# print("The Avarage Of Entered Number Is :",a**2+b**2)

# name = "Vipin"
# nameshort = name[0:2]
# print(nameshort)

# a = "abcgdyedgud"
# mnm = a[1: 8:3]
# print(mnm)

# name = "yadav vipin_10"
# print(len(name))
# print(name.endswith("0"))
# print(name.endswith("1"))
# print(name.startswith("Y"))
# print(name.capitalize())
# print(name.title())


# name =input("enter your name : ")
# print(f"Good Afternoon {name}")

# print(len(name))
# name = "deepak yadav"
# print(name.replace("yadav","YadaV")) 

# --------------><---------------------
# list and tuples ------------  new topic starts from here 

# Dost = ["Apple","Deepak",67555,"Vipin","Shailesh","Jhon"]
# print(Dost[3]) #list can be change but we cannot do this in strings LIST are flexible


# Dost[2] = "krishn"
# print(Dost[2])
# print(Dost[3:5])
# Dost.append("Vijay")
#num= [1,34,65,89,54,332,11]
# num.sort()
# num.reverse()
# num.insert(3,566) # we had inserted 566 at the position of index 3 (in codeing counting start from 0)
#num.pop(2) # pop helps us to delete a part in list at a perticuler place or location. like here we had put 2 which means i want to delete the number at the no.2(3) position  
#num.remove(34) #here we had removed the number that we want that this should nott be in the list and in this we need to put element that we wamt to remove not the position of elememt
#print(num)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------TUPlES-------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#new topic 

#the  basic difference between tubples and list are that tuples are immutable same as string.
# a=(1,674,67,5,4,"deepak")
# print(type(a))
# no=a.count("deepak")
# no = a.index(5)
# print(no)
# repeated = a*3
# print(repeated)

# Marks = []
# f1 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f1)
# f2 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f2)
# f3 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f3)
# f4 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f4)
# f5 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f5)
# f6 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f6)
# f7 = input("Enter the names of  yourr fav Marks :")
# Marks.append(f7)

# print(Marks)

# Marks = [] 
# f1 = int(input("Enter The Marks :")) #here we had return  int(input("Enter Your Marks")) Here we had added int becz it was a string so we had changed it to integer so that we can print numbers.
# Marks.append(f1)
# f2 = int(input("Enter The Marks :"))
# Marks.append(f2)
# f3 = int(input("Enter The Marks :"))
# Marks.append(f3)
# f4 = int(input("Enter The Marks :"))
# Marks.append(f4)
# f5 = int(input("Enter The Marks :"))
# Marks.append(f5)
# f6 = int(input("Enter The Marks :"))
# Marks.append(f6)
# f7 = int(input("Enter The Marks :"))
# Marks.append(f7)
# Marks.sort()
# print(Marks)

# <<<<<<<<<<<<<<<<<<<-----------SETS And Dictionary-------------->>>>>>>>>
#Chapter 5.

# marks = {
#     "Deepak": 100,
#     "Vipin": 98,
#     "Shailesh": 89
# }
# print(marks.keys())
# print(marks.items())
# print(marks.values())
# marks.update({"deepak":98,"Shubham":86})
# print(marks,type(marks))
# print(marks.get("Deepak")) #line 121 and 122 will return same results but the diffence is that if we put a name which is 
#not present in your dictionary then line 122 will return an error but the linne 121  will return None.
#This is the basic difference between this two(its an interview question as well)
# print(marks["Deepak"])
# print(marks)
#to create an empty dictionary -->> d={} it's an empty dictionary.

#now,Sets --> This Is Collection on non-repeatitive elements.
#to create an empty set-->>  e=set() #it's an empty set
# print(type(e))
#set={1,2,3,4,5,5,5} #in sets repeatition are not allowed and if had repeated any number multiple times then the compiler will 
#read it or consider it once.
# s={1,2,3,4,5} 
# s.add(56)---->> used to add the elements to the sets.
# s.remove(3)--->> used to remove any element from the sets.
#s.clear()--->> it is used to clear the sets
# print(s,type(s)) --->> sets are not in ordered they are unordered 
# they are also unindexed which means they cannot be accessed by the index.
# they can't have duplicate values.
# len1= len(s)--->> this is used to check the lengths of the  given sets.
# print(len1)
#s.union()--->>returns with elements from both the sets.
# s1 = {1,2,3,4,5}
# s2 = {11,22,3,42,53}
# print(s1.union(s2))
#s.intersection()---->> returns with the common elements in both the sets.
# print(s1.intersection(s2))
  
#------------->>>>>>>>>>>>>>>> Chapter-5 pracctice set <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------
# Question No.1 
# words = {
#     "help" : "maddat",
#     "Aam" : "Mango",
#     "billi" : "Cat"
# }
# word = input("Enter The Word You Want Meaning Of :-")

# print(words[word])

#Question No.2
# s = set()
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))
# n = input("Enter The Number :  ")
# s.add(int(n))

# print(s)

# --------------------------------
#question no.3

# s={18,"18"}

# s.add(18)
# s.add("18")
# print(s,type(s))
# -----------------------------------
#question no.4
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))


#question 5

# s={}
# print(type(s))

#question 6
# d={}
# name = input("Enter Your  Friends Name: ")
# lang = input("Enter The Name Of Your Language: ")
# d.update({name : lang})
# name = input("Enter Your  Friends Name: ")
# lang = input("Enter The Name Of Your Language: ")
# d.update({name : lang})
# name = input("Enter Your  Friends Name: ")
# lang = input("Enter The Name Of Your Language: ")
# d.update({name : lang})
# name = input("Enter Your  Friends Name: ")
# lang = input("Enter The Name Of Your Language: ")
# d.update({name : lang})
# name = input("Enter Your  Friends Name: ")
# lang = input("Enter The Name Of Your Language: ")
# d.update({name : lang})

# print(d)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# new chapter 
# conditionals 

# a=int(input("Enter Your Age : "))

# if(a>=18):
#     print("You Are An Adult ")

# elif(a<0):
#     print("Age Can't Be Negative So Please Enter The Age In Postive :)")

# else:
#     print("You Are Not An Adult ")

# a=int(input("Enter The Age : "))

# if(a>=18):
#     print("Greater")
# else:
#     print("lesser")

# a1= int(input("Enter The Number  1: "))
# a2= int(input("Enter The Number  2: "))
# a3= int(input("Enter The Number  3: "))
# a4= int(input("Enter The Number  4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest Number Entered By User Is A1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest Number Entered By User Is A2: ",a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest Number Entered By User Is A3: ",a3)

# elif(a4>a2 and a4>a3 and a4>a3):
#     print("Greatest Number Entered By User Is A4: ",a4)

# marks1=int(input("Enter Your Marks1: "))
# marks2=int(input("Enter Your Marks2: "))
# marks3=int(input("Enter Your Marks3: "))

# total_Percentage=(100*(marks1+marks2+marks3))/300

# if(total_Percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed !!!\n",total_Percentage)
# else:
#     print("You Are Failed,Try Again Next Time !!!\n",total_Percentage)

# p1="Buy Now"
# p2="Free"

# message = input("Enter The Comment : ")

# if((p1 in message) or (p2 in message)):
#     print("This  Comment Is  Spam!! Stay Away From This Type Of Comment")
# else:
#     print("You Are Safe This  is Not A Spam!!")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-----------LOOPSSS------------->>>>>>>>>>>
# while Loopss
# i = 0

# while(i<5):
#     print("Harry")
#     i +=1

# l = [1,"Deepak","Yes","Noo","Shubham"]

# i=0

# while(i<len(l)):
#     print(l[i])
#     i+=1


#for loopss

# for i in range (4):
#     print(i)

# l=[1,2,3,4,5,6,7] ---------Loops With List
# for item in l:
#     print(item)

# t=(2,3,4,5,454,54) ------Loops With Tuples
# for item in t:
#     print(item)

# s= "Deepak" -----------Loops With Strin
# for item in s:
#     print(item)

# for i in range(0, 77, 7): 
    # print(i)


#for loops with Else: 


# l=[1,2,3,4]
# for item in l:
  #  print(item)
#else:
 #   print("Done") #This will always be printed when we are printing the for loop but the condition is that it will print after  the complition of for loops.


#break and coontinue and pass Statements 

# loop with break

# for i in range(100):
#     if(i==67):
#         break #when we use break it exits the loops Instant  
#     print(i)

# # Loop With continue

# for i in range(100):
#     if(i==67):
#         continue   #when we use continue then it will skip the number that we have entered in condition and print the remainning part of loop
#     print(i)

#Loops With pass

# for i in range(243):
#     pass #--- if we use pass n any code then it will skip the hole code like if we want leave the code at half work and we want to do diff. code but while 
# #running the code there should be any error in such case we use pass function which means leave that code on half work and shift to different code. 





# for i in range (675):
     #pass ----> if i will not  write  this then the code  will give  error and pass means that  i want to skip this part of code or i will do it later


# n = int(input("Enter The Number : "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n * i}")

# <<<<<<<<<<<<<<<<<<<<<<<<<------------------Practice Questions Of Loops---------------->>>>>>>>>>>>>>>

# n= int(input("Enter the number: "))

# for  i in range(1,11):
#   print(f"{n} X {i} = {n * i }" ) # printing of table input  formm user.


# Q.2 --->
# l=["Vipin","Vijay","Deepak","Shailesh"]

# for name in l:
#   if(name.startswith("V")):
#       print(f"Hello {name}") #------> Finding The Name Of Person With The Starting Alphabate 'V'

# Q.3
# n = int(input("Enter the number: "))

# i = 1

# while(i<11):

#   print(f"{n} X {i} = {n * i }" ) # printing of table input  formm user.

#   i+=1
# print the table with while loop

# Q.4

# n= int(input("Enter the number: "))

# for  i in range (2,n):
#   if(n%i)==0:
#     print("The Number Is  Even")
#     break
# else:
#   print("The Number Is prime")    
# Q.5

# n = int(input("Enter The Number : "))
# i = 1
# sum = 0
# while(i<=n):
#   sum += i
#   i += 1

# print(sum)

# Q.6

# n = int(input("Enter The Number: "))

# for i in range(1,n+1):
#   print(" "*(n-i),end="")
#   print("*"*(2*i-1),end="") # If We Don't  Want Next Line In Print Statements Then we write end="" 
#   print("")

#Q.10
# To Print Table In Reverse Order 

# n =  int(input("Enter The Number : "))

# for i in range(1,11):
#     print(f"{n} X {11-i} = {n * (11-i)}")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------FUNCTIONS AND RECURSION----------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#when we want to use any part of code multiple times then we create function which make our work easy.


#FUNCTION DEFINATION-----------
                            # | 
# def avg():   ------------------------------->>>> Here we had given a name to a function which we can use further in the  codes like if we want to use this part of  code then we have to just write the name of funtion insted of hole code.
#     a = int(input("Enter The Number : "))
#     b = int(input("Enter The Number : "))
#     c = int(input("Enter The Number : "))

#     average = (a+b+c)/3
#     print(average)


# avg() ------------->>>>>>. Calling the function. (also called as functionn call)


# n = input("Enter Your Name : ")
# def gooday():
#     print("Gooday Mr."+ n) #-------------> So Here to print the user input we can use a + symbols or  a ,(Comma) :- print("Gooday Mr."+ n) OR  print("Gooday Mr.",n)

# gooday()


#parameters 
# def gooday(name,ending): #------------> here we had passed an parameter which helps to print the name Vipin.
#     print("Gooday Mr.\n" + name + "\t", ending)

# gooday("Vipin", "Bye!!!")  ----------->>>>>>>>>>>>>> We Can Pass Multiple Aurguments In a Single Loops Or Set Of Code.



# Recursion Is A Function Which Calls ItSelf.

# def factorial(n):
#   if (n==1 or n ==0):
#     return 1
#   return n * factorial(n-1)

# n = int(input("Enter The Number : "))
# print(f"Factorial Of The Number You Have Entred Is : {factorial(n)} ")

# a = int(input("Enter The  Number a : "))
# b = int(input("Enter The  Number b : "))
# c = int(input("Enter The  Number c : "))

# def greatest(a,b,c):
#   if(a>b and a>c):
#     return a
#   elif(b>a and b>c):
#     return b
#   elif(c>b and c>a):
#     return c

# print("The Greatest Number Is : " , greatest(a,b,c))

# n = int(input("Enter The Number : "))
# def sum(n):
#   if(n==1):
#     return 1
#   return sum(n-1) + n
# print("The Sum Of Entered Number Is : ", sum(n))


# n=int(input("Enter The Number: "))
# def patter(n):
#   if(n==0):
#     return
#   print("*"* n)
#   patter(n-1)

# print(patter(n))


