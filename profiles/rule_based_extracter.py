import re
__test__ = True
server_find_length = 5

def extract_server_info(utterance: str, slots):
    if '1080' in utterance:
        start = utterance.find('1080') + 4
        end = start + server_find_length
        res = re.search('[1-6]', utterance[start:end])
        if res is not None:
            if not __test__:
                slots.server.name = '1080ti-{}'.format(res[0])
            else:
                print(' searched string: ', utterance[start:end], '\n', 'server name: ', '1080ti-{}'.format(res[0]))
        else:
            if __test__:
                print('1080ti not fully detected')

    elif '2080' in utterance:
        start = utterance.find('2080') + 4
        end = start + server_find_length
        res = re.search('[1-2]', utterance[start:end])
        if res is not None:
            if not __test__:
                slots.server.name = '2080ti-{}'.format(res[0])
            else:
                print(' searched string: ', utterance[start:end], '\n', 'server name: ', '2080ti-{}'.format(res[0]))
        else:
            if __test__:
                print('2080ti not fully detected')

    elif 'titan' in utterance:
        start = utterance.find('titan') + 5
        end = start + server_find_length
        res = re.search('1|3|rtx', utterance[start:end])
        if res is not None:
            if not __test__:
                slots.server.name = 'Titan-{}'.format(res[0].upper())
            else:
                print(' searched string: ', utterance[start:end], '\n', 'server name: ', 'Titan-{}'.format(res[0].upper()))
        else:
            if __test__:
                print('Titan not fully detected')

def extract_disk_info(utterance, slots):
    pass

def extract_user_info(utterance, slots):
    pass