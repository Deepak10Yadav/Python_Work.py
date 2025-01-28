n = input()
count = 0 
i = 0 
while i < len(n):
    c = n[i]
    if c == 'a' or c == 'e' or c == 'o' or c == 'i' or c == 'u':
     count += 1
    i += 1
print(count)