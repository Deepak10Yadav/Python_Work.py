a = 67
def fun():
    global a #changes The Variable Instaant..  (output()) if we remove global part then the output will the variable that we had created in start of code like here a = 67
    # will be printed two times 
    a = 6776
    print(a)

fun()
print(a)

# Variable Which We Can Be Use At Multiple Line's In The Code.