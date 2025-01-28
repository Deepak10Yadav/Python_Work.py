'''Decorators are the functions which just modify the given code and return them.
or 
it  is a function which take's another funtion and update it or modify it and then return it. 
to use decorators we need to create them and use the '@' symbaol  to use the function inside it.
'''
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure

# # Syntax := def decorator_name(func):
#     def wrapper(*args, **kwargs):  
#         # Add functionality before the original function call
#         result = func(*args, **kwargs)
#         # Add functionality after the original function call
#         return result
#     return wrapper


# @decorator_name
# def function_to_decorate():
#     # Original function code
#     pass

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ex-1 :=
def tt(fx):    # here we had created the ddecorated function 
    def mfx():
        print("Welcome")
        fx()
        print("Thank You!!")
    return mfx

@tt   #here we had used it (or) had called the decorator function.
def hello():
    print("Hello World")

hello()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ex-2 :=

def greet(func):
    def deco():
        print("Welcome01")
        func()
        print("Thank You Very Much To Use Our Function!!")
    return deco

@greet
def heyy():
    print("Heyyy My Self Deepak")
heyy()
# greet(heyy)() #method  2 of callng  the decorated function




# decorated function ko call krne ka 2 ways hai :
# no.1 := Haam Direct Usko '@' wale se use kare.
# no.2 := jo name se hamne use create kiya hai usse use krle. callinf=g ke time pr.
# lakin ekbaar hamne @ wala use kiya tho second wala use nhi kr sakte..



# agar hame kabhi koi arguments lena hai tho ham *args and **kwargs use krte hai check line-9
# *agrs take the agruments in the form of tuples and **kwargs take the arguments in the form of dictionary


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# ex := 3 (with arguments)


def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)
