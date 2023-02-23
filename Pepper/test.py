import qi

dict1 = {
    'a': 1,
    'b': 2,
    'c': 'ciao',
    'd': True
    }

a = dict1.get('a')
b = dict1.get('b')
e = dict1.get('e')


def print_value1():
    print('Value1')


def print_value2():
    print('Value2')


actions = {
    'print_value1': print_value1,
    'print_value2': print_value2
}

resp = {'plan': ['print_value1', 'print_value2']}

action_list = resp['plan']

for action in action_list:
    actions[action]()