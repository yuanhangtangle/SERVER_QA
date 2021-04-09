#!/usr/bin/python3
import utils

Available_Slots = ['SERVER', 'USER_NAME', 'USER_PASSWORD']


class Server:
    Available_Slots = ['name', 'disk']

    def __init__(self, name: str, disk: str):
        self.name = str(name)
        self.disk = str(disk)

    def clear(self) -> bool:
        return utils.clear(self)


class User:
    Available_Slots = ['name', 'password']

    def __init__(self, name: str, password: str):
        self.name = str(name)
        self.password = password

    def clear(self) -> bool:
        return utils.clear(self)


class SlotValues:
    def __init__(self):
        self.server = Server()
        self.user = User()

    def clear(self):
        return utils.clear(self.server) and utils.clear(self.user)

if __name__ == '__main__':
    s = Server('n', 'p')
    for key in s.__dict__.keys():
        print(key, s.__dict__[key])
