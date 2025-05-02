import numpy as np
arr1d = np.array([1,2,3,4,5,67])
print(arr1d)
arr2d = np.array([[2,3,4],[1,2,3]]) # if we want to print this array then we need to put both the arrays in a single bracket else it will give an error same goes with n numbers of arrays.
print(arr2d)

# List Vs Numpy Array
list = [1,2,3,4]
print(list *2)

arr2 = np.array([1,2,3]) # element wise multiplication
print(arr2*2)

import time # to calculate the time 
start = time.time()
list = [i*2 for i in range(100)]
print(time.time() - start)

# creating array

zeros = np.zeros((3,4))
print(zeros)

full =  np.full((3,3),6) # if we need a single constant matrix we use full method to create an array. create a matrix of 3 by 3 with all value of 6.
print(full)

random = np.random.random((2,3)) # create a matrix with random constants
print(random)

sequence = np.arange(0,10,2) #here we give a range to print. it will print like o to 10 by the gap of 2 numbers. expexxted output :- [0 2 4 6 8]
print(sequence)


''' Vector , Matrix and Tensor'''

vector = np.array([1,2,3,4,5,6]) # the simple array is known as vector array
print(vector)

matrix = np.array([[1,2,3],
                  [4,5,6]])
print(matrix)

'''when we needd to deal with multiple numbers of array we prefer to use tensor rather than matrix or vector or numpy'''
Tensor =  np.array([[[1,2],[3,4],
                    [5,6],[7,8]]])
print(Tensor)


# Arrays Properties
arr = np.array([[1,2,3],[4,5,6]]) # Numpy Arrays Has Multiple Properties.
print("Shape",arr.shape) # shapes is a properties.
print("Dimensions",arr.ndim)
print("Size",arr.size)
print("Data-Types",arr.dtype)

#Array Reshaping.
arr = np.arange(12)
print("Original Array-->",arr)

reshaped = arr.reshape((3,4)) #converting the  above array in matrix.
print("After Reshape-->",reshaped)

#  if the array is in matrix form and we need to convert it in flat then..
flat = reshaped.flatten()
print("Flated Array-->",flat)

#  ravel (returns view of original array , insted of copy of the array)
raveled = reshaped.ravel()
print("Raveld array-->", raveled)

# Transpose of the matrix
transpose  = reshaped.T
print("\n Transpose Matrix-->",transpose)

'''--------------------------------------------------------------------------------------------------------------------------------'''

# Numpy Array Opreations
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic Slicing-->",arr[2:7]) #--> here we create a new array from the existing array.
print("With Steps",arr[1:6:2]) # prints the array with skipping 2 values.
print("Negative Indexing",arr[-3]) # it will print the value from last position minus the number.

#indexing Slicing on 2D array
arr = np.array([[1,2,3],  # indexing numbers starts from 0.
                [4,5,6],
                [7,8,9]])
print("Specific Element", arr[1,2])
print("Entire Row-->",arr[1])
print("Entire Column-->",arr[:,1]) # here ':' refers to entire row.

# Sorting the arrayy..


unsorted = np.array ([3,4,6,8,3,2,2])
print("Sorted Array",np.sort(unsorted))

array_2d_unsortedd = np.array([[1,6],[5,9],[8,2]])
print("Sorted 2D Array by Column-->",np.sort(array_2d_unsortedd, axis=0)) # top to bottom
print("Sorted 2D Array by Row-->",np.sort(array_2d_unsortedd,axis=1)) #Left to right

#'''Filtering Array'''---------------------------------------------------------------------------------------------------------------
numbers= np.array([1,2,3,4,5,6,7,8,9,10])
even_number = numbers[numbers % 2 == 0] # Numppy Allows Us to write expressions.
print(even_number)

# Filter With Masks
mask = numbers > 4 # the expressions that we integreate between the normal code  is known as mask. example :- Line 103
print("Numbers Greater Than 4:",numbers[mask])

'''Fancy Indexing vs np.Where()----------------------------------------------------------------------------------------------------------------'''
indices  = [0,2,4] # here we had entered the index of elements we want to print
print(numbers[indices]) # here we had integrated the indicies in numbers array from which we get output.

#indexing By Using Array.
where_result = np.where(numbers >= 5)
print("Np where",numbers[where_result])

# creating an array at some condditions---------------------------------------------------------------------------------------------------------------
condition_Array = np.where(numbers > 22,numbers*2,numbers)  # it mostly carry true or false values.
# condition_Array = np.where(numbers > 4,"true","false")  # it mostly carry true or false values.
'''
if(numbers > 5):
     numbers *4
else:
     numbers

''' # this is the explanations of the Above code in line 119 
print(condition_Array)

'''-------------------------Adding And Removing  of Data---------------------------------------------------------------------------------------------'''
arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])

# add = arr3 + arr4  # if we use this way to add the elements then we will get a different addition ouput it will direcctly add the elements.
# print(add)
add = np.concatenate((arr3 , arr4)) # it will give the output [1,2,3,4,5,6]
print(add)

'''Array Compatibility'''


a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

print("Compatibility",a.shape == b.shape) # it will return a boolean value.


original = np.array([[1,2],[3,4]])
new_row = np.array([[5,6],[7,8]])

# to add rows we use vstack --> v = vertical stack.
with_new_row = np.vstack((original,new_row))
print(original)
print(with_new_row)

new_col = np.array([[9],[10]])
with_new_col = np.hstack((original,new_col))
print(with_new_col)

'''delete oprations'''

arr = np.array([1,2,3,4])
deleted = np.delete(arr,2) #here two is index value from which we want to delete the element.
print(deleted)

'''vector Operations'''

vector1  = np.array([1,2,3,4,5])
vector2  = np.array([6,7,8,9,10])

print(vector1+vector2)
print(vector1*vector2)
# dot product 
print("dot product",np.dot(vector1,vector2))

angle_of_dot = np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))) #formula of getting angle
print(angle_of_dot)