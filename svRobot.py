from slotValues import SlotValues
from NLU import NLU
import os
import utils
import random

__test__ = utils.set_test_info(os.path.basename(__file__))

class SVRobot:
    def __init__(self):
        self.nlu = NLU()
        self.slots = SlotValues()
        self.response = ""
        self.raw_input = ""
        self.epoch = 0
        self.state = ""
        self.confirm = False
        if __test__:
            print("===== Testing Mode Started =====")
        self._say_hello()

    def start(self):
        while True: # remain: end it?
            server_robot.get_user_utterance()
            server_robot.extract_info()
            server_robot.track_state()
            server_robot.take_action()

    def initialize(self):
        self.slots.clear()
        self.state = None
        self._say_hello()
        self.confirm = False

    def get_user_utterance(self):
        self.nlu.input(self.response)
        self.raw_input = self.nlu.utterance
        self.nlu.preprocess()

    def extract_info(self):
        self.nlu.extract_info()

    def track_state(self):
        if self.nlu.slots.intent.name != 'chit_chat' and self.slots.intent.name != self.nlu.slots.intent.name: # intent changed
            self.initialize() # remain: maybe we can retain some information
            self.slots.fill_from(self.nlu.slots)  # includes intent

        elif self.state == 'server_info':
            self.slots.server.name = self.nlu.slots.server.name
        elif self.state == 'disk_info':
            self.slots.disk.name = self.nlu.slots.disk.name
        elif self.state == 'user_name_info':
            self.slots.user.name = self.raw_input
        elif self.state == 'user_password_info':
            self.slots.user.password = self.raw_input
        elif self.state == 'confirm':
            self.confirm = 'y' in self.nlu.utterance

        '''if __test__:
            print("===== SVRobot =====")
            self.slots.print()
            print("state =", self.state)'''

    def take_action(self):
        if self.slots.intent.name == 'add_user':
            # maybe we need more info
            if self.slots.server.name is None:
                self._ask_server_info()
            elif not utils.is_filled(self.slots.user):
                self._ask_user_info()
            else:
                if self.state != 'confirm':
                    self._confirm_user_info()
                elif self.state == 'confirm' and self.confirm:
                    self._add_user()
                    self.initialize()
                elif self.state == 'confirm' and not self.confirm:
                    self.slots.user.clear()
                    self._ask_user_info()


        elif self.slots.intent.name == 'mount_disk':
            if self.slots.server.name is None:
                self._ask_server_info()
            elif self.slots.disk.name is None:
                self._ask_disk_info()
            else:
                self._mount_disk()
                self.initialize()
        else:
            self._say_hello()

    def _say_hello(self):
        #if self.epoch == 0:
        self.response = "需要我为您做什么？我目前能够提供挂盘、开账号等服务\n"
        self.epoch += 1
        '''
        else:
            self.response = "还需要我为您做什么？"
        '''

    def _add_user(self):
        if __test__:
            print(
                "\n===== Add user ===== \nname = {}\npassword = {}\n".format(
                    self.slots.user.name,
                    self.slots.user.password
                )
            )
        else:
            pass # remain

    def _mount_disk(self):
        if __test__:
            print(
                "Mount disk {} to server {} successfully".format(
                    self.slots.disk.name,
                    self.slots.server.name
                )
            )
        else:
            pass # remain

    def _ask_server_info(self): # remain: why not just check all the servers and disks ???
        if self.slots.intent.name == 'mount_disk':
            if self.state != 'server_info':
                self.response = "哪个服务器的盘掉了？\n"
            else:
                self.response = "我们组没有这个服务器vo，您确认一下是哪个服务器的盘掉了?\n"

        elif self.slots.intent.name == 'add_user':
            if self.state != 'server_info':
                self.response = "您希望在哪个服务器上注册账户？\n"
            else:
                self.response = "我们组没有这个服务器vo，您确认一下是哪个服务器?\n"

        self.state = 'server_info'

    def _ask_disk_info(self): # remain: why not just check all the servers and disks ???
        if self.state != 'disk_info':
            self.response = "哪个盘掉了？\n"
        else:
            self.response = "找不到这个盘vo，您确认一下是哪个盘掉了?\n"
        self.state = 'disk_info'

    def _ask_user_info(self):
        if self.slots.user.name is None:
            self.state = 'user_name_info'
            self.response = "请输入你希望使用的 用户名，务必准确输入：\n"

        # elif to keep priority
        elif self.slots.user.password is None:
            self.state = 'user_password_info'
            self.response = "请输入你希望使用的 用户密码，务必准确输入：\n"

    def _confirm_user_info(self):
        self.state = "confirm"
        self.response = "请确认您的用户名和密码：\n用户名： {}\n密码：{} \n[y/n]\n".format(
                self.slots.user.name,
                self.slots.user.password
            )

if __name__ == '__main__':
    server_robot = SVRobot()
    server_robot.start()