import json

def serr(email):
    with open('data.json', 'r') as rf:

        users = json.load(rf)
        return users[email][0]