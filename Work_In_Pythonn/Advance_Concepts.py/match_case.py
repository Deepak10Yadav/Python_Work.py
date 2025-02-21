a = int(input("Enter The Number From 200 , 404 , 500 := "))
b = int(input("Enter The Number From 200 , 404 , 500 := "))
def status(sta):
    match sta:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Error"
        case _:
            return "Unkonw Status"



def tut(r):
    match r:
        case 900:
            return "found"
        case Exception as ValueError:
            return "ValueError"
        
print(status(a))
print(tut(b))
