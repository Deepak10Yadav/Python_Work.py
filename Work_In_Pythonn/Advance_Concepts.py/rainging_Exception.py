a = int(input("Enter The Number:"))
b = int(input("Enter The Number:"))

if( b==0 ):
    raise  ZeroDivisionError("Sorry We Cannot Divide It By 0") # to create a error we use keyword raise (type_of_error_name)
else:
    print(f"The Divion Is {a/b}")