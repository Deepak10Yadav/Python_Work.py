import json
def data_load(filename):
    with open("data.json") as f:
        return json.load(f)
    
def ppl_you_may_know(user_id, data):
    user_frineds = {}
    for user in data['users']:
        user_frineds[user[id]] = set(user['friends'])

# load data
data = data_load("data.json")
user_id = 1
recc = ppl_you_may_know(user_id,data)
print(recc)