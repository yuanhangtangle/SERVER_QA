#!/usr/bin/python3
import utils

class Name_Entity:
    def __init__(self, name: str = None):
        self.name = str(name)

    def clear(self):
        for key in self.__dict__.keys():
            self.__dict__[key] = None

class Intent(Name_Entity):
    def __init__(self, name: str = None):
        super().__init__(str(name))

class Server(Name_Entity):
    def __init__(self, name: str = None):
        super().__init__(str(name))

class Disk(Name_Entity):
    def __init__(self, name: str = None):
        super().__init__(str(name))

class User(Name_Entity):
    def __init__(self, name: str = None, password: str = None):
        super().__init__(str(name))
        self.password = str(password)


class SlotValues:
    def __init__(self):
        self.intent = Intent()
        self.server = Server()
        self.disk = Disk()
        self.user = User()
        # self.confirmed = False # remain: maybe we want the user to confirm

    def clear(self):
        for key in self.__dict__.keys():
            self.__dict__['key'].clear()

    def fill_from(self, sv):
        for subslot in self.__dict__.keys():
            self.__dict__[subslot] = utils.fill_obj(
                self.__dict__[subslot],
                sv.__dict__[subslot]
            )
    def print(self):
        for subslot in self.__dict__.keys():
            print('-'*20, subslot, '-'*20)
            utils.print_slots(self.__dict__[subslot])

if __name__ == '__main__':
    sv = SlotValues()
    sv.server.name = '1080ti'
    sv.disk.name = 'nlper_data'
    sv.user.password = 'test_pw'
    sv.user.name = 'test_name'