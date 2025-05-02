a = input("Enter The Value for a := ")
b = input("Enter The Value for b := ")
op = input(" (+,-,*,/)") 
for op in op:
    if op == '+':
        print(int(a)+int(b))
    if op == '-':
        print(int(a)-int(b))
    if op == '*':
        print(int(a)*int(b))
    if op == '/':
        print(int(a)/int(b))

