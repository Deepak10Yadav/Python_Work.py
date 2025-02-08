'''Multithreading'''
import threading #to use threading method we need to use import it.
import time

def func(seconds):
    print(f"The Program Sleeps for {seconds}")
    time.sleep(seconds)

# here we had called the function and the function will run in the given time period.
# python program runs each line one by one. so to run all this at same time we use thread method
#Normal code

# func(1)
# func(4)
# func(6)

# same code using threads
# here we had used multi threading for printing the output.

t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[4])
t3 = threading.Thread(target=func, args=[6])

t1.start()
t2.start()
t3.start() # after using this all the thing will be printed at a same time.