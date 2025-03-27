'''Hash Tables or a Hashmap is a type of data structure that maps keys to its value pairs
key is generated using hash function'''
'''Element of dict is not order and they can be change'''

#creating a dict
'''method 1'''
my_dict= {'deepak':'001','vipin': '898'}
print(type(my_dict))
# method - 2 
new_dict=dict(my_dict) # here we had passed the dict named my_dict as parameters. so that there value must be  pasted from my_dict.
print(new_dict)
type(new_dict)

#nested dictionaries 
emp = {'Employee':{'Messi':{'id': '003','Salary':'12909022'},'Neymar':{'id' :'090','Salary ':'834823478'}}} #here the employee is main element(main dict) 
print(emp)

#Operations On Hash-Tables
#1.  Accessing Items 
print(my_dict.keys()) # to get keys
print(my_dict.values()) # to get values
print(my_dict.get('vipin')) # to get values for a selected element.

# Accessing by using for-loop:=
# keys 
for x in my_dict:
    print(x) # it will return all keys in the dict.

# values
for  x in my_dict.values():
    print(x) # it will return all values in the dict.

for x,y in my_dict.items():
    print(x,y) # it will return keyss as well as values of that key.

#2. Updates The Values



