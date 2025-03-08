'''
Stack Follows LIFO Function := Last in First Out  
Implementation Of Stack Using List
'''
stack = [] #Empty List.
stack.append("Heyy")
stack.append("Myself")
stack.append("Deepak")
print(stack)
print(stack.pop())
print(stack)

'''Implementation Of Stack Using Dequeue
In Dequeue The Apppend And Pop Methods Are Faster Compare to  Lists.'''

from collections import deque
stack  = deque()
stack.append("Hello")
stack.append("EveryOne")
stack.append("Goodmorning")
print(stack)
print(stack.pop())
print(stack)

'''Stack Implementation Using Queue
It Has Some Additional Function But Works As A Stack
It Follows LIFO Queue'''

from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put(5)
stack.put(6)
stack.put(4)
print(stack.full())
print(stack.qsize())
stack.get()
print(stack)