import utils
import json
from SVRobot import SVRobot
from slotValues import SlotValues
from profiles import rule_based_extracter as RBextracter

class NLU:
    Available_Slots = ['intent','server_name','disk','user_name','password']
    Available_intents = ['chit_chat', 'mount_disk', 'add_user']

    def __init__(self):
        self.slots = SlotValues()
        self.intent = 'chit_chat'
        with open("profiles/cmdpw.json", 'r') as f:
            self.config = json.load(f)

    def input(self, response: str):
        self.utterance = input(response)

    def preprocess(self):
        self.utterance = self.utterance.lower()

    def extract_info(self):
        #check intent
        self._extract_intent_info()
        self._extract_slot_info()

    def fill_slots(self, svRobot: SVRobot):
        pass

    def _extract_intent_info(self):
        for intent in self.config['available_intents']: # sorted by priority
            for token in self.config['intents'][intent]['tokens']: # mathc tokens
                if token in self.utterance:
                    self.intent = intent
                    break # priority


    def _extract_slot_info(self):
        # Remain slots information is extracted based on detected intent. This may be modified.
        for slot in self.config['intents'][self.intent]['slots']:
            if slot == 'server':
                RBextracter.extract_server_info(self.utterance, self.slots)
            elif slot == 'disk':
                RBextracter.extract_disk_info(self.utterance, self.slots)
            elif slot == 'user':
                RBextracter.extract_user_info(self.utterance, self.slots)


