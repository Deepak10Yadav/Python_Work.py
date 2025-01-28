try:
    a = int(input("Enter :"))
    print(a)
except Exception as e:
    print(e)
else:
    print("Try Was Successfull") #this will be get runned only when the try part was successfull.
