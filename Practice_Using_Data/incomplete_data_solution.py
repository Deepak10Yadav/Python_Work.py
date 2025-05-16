import json
def clean_data(data):
    #removing the data without name.
    [user for user in data['users'] if user['name'].strip()] #The strip() function in Python is used to remove leading and trailing characters from a string.
    # to remove duplicates 
    for user in data['users']:
        user["friends"] = list(set(user['friends']))
    # to remove inactive user
    data['users'] = [user for user in data['users']if user['friends']or user ['liked_pages']]
    # to remove duplicates from the data.
# to print data.
data = json.load("incomplete_data.json")
data = clean_data(data)
json.dump(data, open("Clean_data.json",'w'), indent=4)
print("Data has been cleaned.")