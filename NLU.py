import utils
import json
import re
import os
from slotValues import SlotValues

__test__ = utils.set_test_info(os.path.basename(__file__))

with open("./profiles/disks.json", "r") as f:
    disks_config = json.load(f)
with open("./profiles/intents.json", "r") as f:
    intents_config = json.load(f)
with open("./profiles/servers.json", "r") as f:
    servers_config = json.load(f)

class NLU:
    def __init__(self):
        self.slots = SlotValues()

    def input(self, response: str):
        self.utterance = input(response)

    def preprocess(self):
        self.utterance = self.utterance.lower()
        for c in ['-', '_']:
            self.utterance = self.utterance.replace(c, '')

    def extract_info(self):
        self.slots.clear()
        self.extract_intent_info()
        # remain: slots depends on intent
        for slot in intents_config[self.slots.intent.name]['slots']:
            if slot == 'server':
                self.extract_server_info()
            elif slot == 'disk':
                self.extract_disk_info()
        if __test__:
            print('===== NLU =====')
            self.slots.print()
    def extract_server_info(self):
        for _key_token in servers_config['available_key_tokens']:
            if _key_token in self.utterance:
                idx = self.utterance.find(_key_token)
                start = idx + len(_key_token)
                end = start + servers_config[_key_token][0] # search length
                res = re.search(servers_config[_key_token][1], self.utterance[start:end]) # match pattern
                if res is not None:
                    aux = res.group(0)
                    if aux in servers_config[_key_token][3].keys():
                        aux = servers_config[_key_token][3][aux]
                    self.slots.server.name = servers_config[_key_token][2].format(aux)
                    # delete the server part in the utterance to avoid mismatch when detecting disk
                    self.utterance = self.utterance.replace(self.utterance[idx: idx + 6], " "*6)
                    if __test__:
                        print("Detect server:", self.slots.server.name)
                        print("masked utterance", self.utterance)
                    break

    def extract_disk_info(self):
        for _disk in disks_config['available_disks']:
            _key = disks_config[_disk]['key']
            _aux = disks_config[_disk]['auxiliary']
            if _key in self.utterance:
                _idx = self.utterance.find(_key)
                _length = _aux[2]
                # remain: without asking for confirm
                if (
                        _aux[1] == 'pre' and
                        _aux[0] in self.utterance[_idx - _length: _idx]
                ) or (
                        _aux[1] == 'post' and
                        _aux[0] in self.utterance[_idx + len(_key): _idx + len(_key) + _length]
                ):
                    self.slots.disk.name = _disk
                    if __test__:
                        print("Detect disk: {}".format(_disk))
                    break

    def extract_intent_info(self):
        for _intent in intents_config['available_intents']:
            if utils.at_least_one_in(intents_config[_intent]['tokens'], self.utterance):
                self.slots.intent.name = _intent
                if __test__:
                    print("Detect intent: {}".format(_intent))
                break

    def extract_user_info(self):
        pass

if __name__ == '__main__':
    nlu = NLU()
    utterance = '{}的{}好像掉了'
    for server in servers_config['available_servers']:
        for disk in disks_config['available_disks']:
            print('-'*20, server, disk, '-'*20)
            nlu.utterance = utterance.format(server, disk)
            nlu.preprocess()
            nlu.extract_info()
            if nlu.slots.server.name != server or nlu.slots.disk.name != disk:
                raise Exception("Something's wrong when testing ", server, disk)







