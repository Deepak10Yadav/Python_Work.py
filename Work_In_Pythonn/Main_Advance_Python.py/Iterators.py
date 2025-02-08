# in this  we convert the list in the iterators like beforr using  the iteratorss function
# Syntax to convert := name = iter(list_name) 
#  iterators will give only one value aat a time.  it will  not  print all the values a time.
numb = [7,6,5,3]
# for i in numb:
#     print(i)
dead = iter(numb) # Syntax to convert
#print(it) # if we print this then we will get the object of the iterators. Not the value.
# to get value we needd to use a inbuilt function called next
print(dead.__next__()) # we use this fucntion to get  our first value or the element
print(dead.__next__()) # if we called it again then it will print the second element of the list.
print(dead.__next__()) # if we called it again then it will print the third element of the list.
print(dead.__next__()) # if we called it again then it will print the fourth element of the list.

''' CREATING OUR OWN ITERATORS'''

#we need two important methods 
# iter method and next
# iter will give us the object of iterator  and next to print the next value or object

class Top:
    def __init__(self):
        self.num = 1 # here we had mention from where our counting will begin.
    def __iter__(self): # here we had created an iter method
        return self
    def __next__(self): # here we had created an next method
        if self.num <= 10: # here we had writen the condition till where we want to print the numbers.
          val = self.num 
          self.num += 1
          return val  
        else:  # to stop the loop we need to raise a exception.
            raise StopIteration
values = Top()
print(values.__next__()) # here we had called the iterator and once's any  number is printed then the same element will not be printed again. output = 1

for z in values:  # here the output = 1 will not get printed becz we had already printed it in line 34.
    print(z)