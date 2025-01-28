# Function created using an expression "Lambda" keyword

# ex - 
# we want to print sqaure of numbers :
# def square(n):
#     return n*n       ---------------->>>>>>>> Method - 1 or normal way  
# print(square(5))
#OUTPUT - 25
# method - 2(by using lambda function)
sqaure = lambda x: x*x  #-----> it will take x and will return x*x
print(sqaure(5))
#OUTPUT - 25


# syntax = lambda arguments: expression


# Qustion
number = [1, 2, 3 ,4]
sqaure = list(map(lambda x:x*x,number))
print(sqaure)

