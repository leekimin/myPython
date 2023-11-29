

data = {"name":"123", "username":"my", "addr":{"addr1":"seoul"}}

class Addr(object):
    addr1 : str

    def __init__(self, addr1):
        self.addr1 = addr1

class User(object):
    name : str
    username : str
    addr : Addr

    def __init__(self, name, username, addr):
        self.name = name
        self.username = username
        self.addr = Addr(addr['addr1'])

import json
#j = json.loads(data)
u = User(**data)

print(vars(u.addr))