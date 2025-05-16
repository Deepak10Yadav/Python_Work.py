import json
def load_data(filename):
    with open("C:/Users/vijay/Downloads/first.py/Practice_Using_Data/data.json", "r") as f:
        return json.load(f)


data = load_data("data.json")


def display(data):
    print("\nData Of Users Details:=")
    for user in data["users"]:
        print(f"ID:{user['id']}.{user['name']} is friends with {user['friends']} and like pages {user['liked_pages']}")
        
    
    print("\nData Of Pages User Likes :=")
    for page in data["pages"]:
        print(f"ID: {page['id']} : {page['name']}")

display(data)