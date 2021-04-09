import utils
from slotValues import SlotValues

class NLU:
    Available_Slots = ['intent','server_name','disk','user_name','password']
    Available_intents = ['chit_chat', 'mount_server', 'add_user']

    def __init__(self):
        self.utterance = None
        self.server_name = None
        self.disk = None
        self.user_name = None
        self.password = None
        self.intent = 'chit_chat'

    def input(self, response: str):
        self.utterance = input(response)

    def preprocess(self):
        pass

    def extract_info(self):
        pass

    def fill_slots(self, slotValues: SlotValues):
        pass