#!/usr/bin/python3
import utils

class Server:
    Available_Slots = ['name', 'disk']

    def __init__(self, name: str = None, disk: str = None):
        self.name = str(name)
        self.disk = str(disk)

    def clear(self) -> bool:
        return utils.clear(self)


class User:
    Available_Slots = ['name', 'password']

    def __init__(self, name: str = None, password: str = None):
        self.name = str(name)
        self.password = str(password)

    def clear(self) -> bool:
        return utils.clear(self)


class SlotValues:
    def __init__(self):
        self.server = Server()
        self.user = User()

    def clear(self) -> bool:
        return utils.clear(self.server) and utils.clear(self.user)

if __name__ == '__main__':
    print('testing message')
    s = Server()
    print(s.__annotations__)
