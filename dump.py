import json
def ser(email,pawode):
    with open('data.json', 'r') as rf:

        users = json.load(rf)

        if email in users:
            if users[email][1] == pawode:
                return 1
            else:
                return 0
        else:
            return 0