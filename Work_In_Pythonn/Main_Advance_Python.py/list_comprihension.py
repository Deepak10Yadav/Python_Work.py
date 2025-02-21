myList = [1,2,3,4,5,6]
# nomal method for squaring.
# square = []
# for item in myList:
#     square.append(item*item)

# same thing we list comprihension:-
square = [i*i for i in myList]


print(square)

list = [1, 2, 3]
square = [i*i+1 for i in list]
multi = [i*4 for i in list]
print(square)
print(multi)