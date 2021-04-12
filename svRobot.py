from slotValues import SlotValues
from NLU import NLU
import utils
import random

class SVRobot:
    Available_greetings = [
            '需要我为您做什么？ 我可以帮助您进行开账号、挂盘等操作'
        ]
    def __init__(self):
        self.nlu = NLU()
        self.slots = SlotValues()
        self.response = ""
        self.state = 'chit_chat'
        self.ask_info = False
        self._say_hello()

    def get_user_utterance(self):
        self.nlu.input(self.response)
        self.nlu.preprocess()

    def extract_info(self):
        self.nlu.extract_info()

    def track_state(self):
        if self.nlu.slots.intent != 'chit_chat' and self.state != self.nlu.slots.intent: # intent changed
            self.state = self.nlu.slots.intent
            self.slots.clear() # remain: maybe we can retain some information

        self.slots.fill_from(self.nlu.slots)


    def take_action(self):
        if self.state == 'add_user':
            if utils.is_filled(self.slots.server) and utils.is_filled(self.slots.user): # ok
                self._add_user()
            elif not utils.is_filled(self.slots.server): # need server info
                self._ask_server_info()
            elif not utils.is_filled(self.slots.user): # need user info
                self._ask_user_info()

        elif self.state == 'mount_disk':
            if utils.is_filled(self.slots.server):
                self._mount_disk()
            else:
                self._ask_server_info()
        else:
            self._say_hello()

    def _say_hello(self):
        self.response = SVRobot.Available_greetings[
            random.randint(0, len(SVRobot.Available_greetings) - 1)
        ]

    def _add_user(self):
        pass

    def _mount_disk(self):
        pass

    def _ask_server_info(self): # remain: why not just check all the servers and disks ???
        template = ''
        if self.state == 'mount_disk':
            template = "{}服务器的{}盘掉了?"
            which_server = '哪个' if self.slots.server.name is None else ''
            which_disk = '哪个' if self.slots.server.disk is None else ''
            template = template.format(which_server, which_disk)

        elif self.state == 'add_user':
            template = "您希望在哪个服务器注册账号?"

        self.response = template

    def _ask_user_info(self):
        if self.slots.user.name is None:
            self.response = '请告诉我你希望使用的用户名:'
        elif self.slots.user.password is None:
            self.response = '请输入您希望使用的用户密码:' #remain: some rules to obey

