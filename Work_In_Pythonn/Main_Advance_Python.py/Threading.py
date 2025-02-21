'''Multithreading'''
import threading #to use threading method we need to use import it.
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"The Program Sleeps for {seconds}")
    time.sleep(seconds)
def main():
 # here we had called the function and the function will run in the given time period.
 # python program runs each line one by one. so to run all this at same time we use thread method
 #Normal code
 time1 = time.perf_counter() # perf_counter() is a keyword that we use to count the time in which the process is completed.
#  func(8) # to print this it will 6 seconds.
#  func(4)# to print this it will 4 seconds.
#  func(1)# to print this it will 1 seconds.
#  time2 = time.perf_counter()
#  print(time2 - time1) # this will give the ddifference or the time that is taken by the process.
#  same code using threads
#   here we had used multi threading for printing the output.

 t1 = threading.Thread(target=func, args=[1]) 
 t2 = threading.Thread(target=func, args=[4])
 t3 = threading.Thread(target=func, args=[6])
#here start leads to just strat the process and move on next process because of this we lead to output of zero seconds.  
 t1.start()
 t2.start()
 t3.start() # after using this all the thing will be printed at a same time.
# if we want to wait for t1 to complete and then move to  t2 to complete and then move to  t3 to complete. the we use join function due to which it waits.
 t1.join()
 t2.join()
 t3.join() #here it will wait till the highest number of agrs we had passed.
 time2 = time.perf_counter() # counts the time.
 print(time2 - time1) # this will give the ddifference or the time that is taken by the process.

def poolingDemo(): # poolthreading is mainly used when we want to deal with major datas
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 4)
        future3 = executor.submit(func, 5)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()