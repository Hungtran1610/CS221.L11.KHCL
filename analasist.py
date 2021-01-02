import re

grammar = {}
key_word = []

def check_key_exist(test_dict, key):
    try:
       value = test_dict[key]
       return True
    except KeyError:
        return False


def grammar_from_string(list_of_string):
    return


def create_grammar(_input_string):
    index = 0
    input_string_cp = _input_string
    while True:
        leafs = re.findall(r'[(][\w+][ \w+]+[)]', input_string_cp)
        if len(leafs) == 0:
            break
        for leaf in leafs:
            tag = re.findall(r'\w+', leaf)
            if index == 0:
                key_word.append(tag[1])
            if check_key_exist(grammar, tag[0]):
                if tag[1:] not in grammar[tag[0]]:
                    grammar[tag[0]].append(tag[1:])
            else:
                grammar[tag[0]] = []
                grammar[tag[0]].append(tag[1:])
            input_string_cp = input_string_cp.replace(leaf, tag[0])
        index += 1
    return


if __name__ == "__main__":
    data = open('./Data/train.txt')
    lines = data.readlines()
    for line in lines:
        create_grammar(line)
    for key, value in grammar.items():
        for rule in value:
            if rule[0] in key_word:
                print(key, '->',"'" + f'''{rule[0]}''' + "'")
            else:
                print(key, '->', ' '.join(rule))