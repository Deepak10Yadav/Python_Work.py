'''
Generator's are used to generate numbers on the spot and here for printing the number we need to first save the number and then call it. the number of time we call 
the number of time it will be printed 
#and here we use yield keyword which help's to terminate the loop for generator  
'''

def createor1():
    i = 1
    while i<=200:
        yield i # yield function is used to terminate the generator loop.
        i +=1   
print(createor1)
x = createor1()   # saving / assinging.
print(next(x)) # calling it to get printed.
print(next(x)) # calling it to get printed.
print(next(x)) # calling it to get printed.
# the number times we will call it the number will be increased by 1 and will get printed.
# generator's helps us to use  less byte's of your platform(laptops,PC,etc.)
# if we want to print all the number then we can write 
print(list(x)) # the list/numbers  will be printed form number 4 because the first three numbers have been printed from line 15,16,17

# it help's us to utilize use memory in best way 