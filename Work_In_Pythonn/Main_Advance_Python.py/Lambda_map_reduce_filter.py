from functools import reduce

''' 
In Python, the map() function is used to apply a specified function to all items in an iterable (such as a list, tuple, etc.) 
and return an iterator that produces the results. It's useful when you want to perform an operation on every element of an iterable, 
and you want to avoid writing a loop
''' 
#MAP Function
# Syntax: map(function, iterable)

l = [1, 2, 3, 4]

sqaure = lambda x: x*x
sqList = map(sqaure,l)
print(list(sqList))

# Output : - [1, 4, 9, 16]
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Filter Example 

'''allows you to filter a sequence (e.g., a list, tuple, or set) based on a given condition.''' 

l1 = [4,5,6,7,8,2]
def even(n):
    if (n%2 == 0):
        return True
    return False

OnlyEven = filter(even,l1)
print(list(OnlyEven))

#Output : - [2, 4, 6, 8]

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Reduce Example 
#to use reduce function we need to import it from  functool.

'''It allows us to apply a specified function to a sequence of elements, progressively reducing it to a single value.'''

def sum(a, b):
    return a + b
print(reduce(sum , l))

mul = lambda x,y : x*y
print(reduce(mul,l))

