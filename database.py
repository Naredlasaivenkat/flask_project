import json


class dbo:
    def insert(self, name, email, password):
        with open('data.json', 'r') as df:
            user = json.load(df)
            if email in user:
                return 0
            else:
                user[email] = [name, password]

        with open('data.json', 'w') as wf:
            json.dump(user, wf, indent=4)
            return 1
