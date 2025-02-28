'''
1. Doubly Linked List Is a List In Which we The Head Node Or The Selectedd Node Is Connected With It's Previous And Next Node.
2. Here Traveral Is  Possible In Both The Directions
Example := 1<-->2<-->3<-->4<-->Null.
'''
#Creating node 
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        # forward Traversal Code
        a= self.head
        while a is not None:
            print(a.data,end="-->")
            a = a.next

        #backward Traversal Code
        a = self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data,end="==>")
            a=a.prev