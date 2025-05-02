# Answers
import numpy as np
x=np.zeros(10)
print(x.size)
print(x.itemsize)
# print(np.info(np.add))
x[5] = 1
print(x)
vector = np.arange(10,49)
print(vector)
array1 = np.array([1,2,3,4,5,6,7,8])
print(np.flip(array1))
matrix = np.array(([0,1,2],
                  [3,4,5],
                  [6,7,8]))
print(matrix)
ind = np.array([1,2,0,0,4,0])
print(np.where(ind!=0))


mat = np.array(([1,0,0],
               [0,1,0],
               [0,0,1]))

print(mat)


mat1 = np.random.random((3,3,3))
print(mat1)

mat10 = np.random.random((10,10))
print(mat10)
print(mat10.max())
print(mat10.min())

vecc2 = np.random.random(30)
print(vecc2)
print(np.mean(vecc2))

array2D = np.ones((2,2))
border = np.pad(array2D,pad_width=1,mode='constant',constant_values=0)
print(border)

'''
pad_width=1 adds one row/column on each side.

mode='constant' fills with a constant value.

constant_values=0 sets that value to 0.
'''

array_ex = np.ones((3,3))
array_border = np.pad(array_ex,pad_width=1,mode='constant',constant_values=0)
print(array_border)

#Queston No. 16 tak Done 

m = np.array(([0,0,0,0,0],
              [1,0,0,0,0],
              [0,2,0,0,0],
              [0,0,3,0,0],
              [0,0,0,4,0]))

print(m)

m1 = np.array(([0,1,0,1,0,1,0,1,0,1],  # this patterns are known as checkborad pattern like chess-board
               [1,0,1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0,1,0],))
print(m1)


np.unravel_index(99,(6,7,8)) #use to find index of any element.



m2 = np.tile([[0,1], [1,0]], (4,4))
print(m2)

m4 = np.random.random(5,5)
print(m4)


m4 = np.random.random((5,5))
# print(m4.ndarray())
normal = (m4 - np.min(m4)) / (np.max(m4) - np.min(m4))
print(m4)
print(normal)



rgba = np.dtype([('r',np.uint8),
                 ('g',np.uint8),
                 ('b',np.uint8),
                 ('a',np.uint8)])

colors = np.array([(255, 0, 0, 255), (0, 255, 0, 128), (0, 0, 255, 0)],dtype=rgba)
print(colors)





matrix1= np.array([[1,2,3],
                   [6,9,3],
                   [4,2,1]])

matrix2 = np.array([[2,3],
                    [4,5],
                    [7,8]])

a1 = np.dot(matrix1,matrix2)
print(a1)

