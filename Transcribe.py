import os
import platform
import re

# rules:
# https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B3%D0%BB%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%86%D0%B8%D1%8F

project_path = {
    'DESKTOP-62BVD4A': 'd:\KPV\Github\Ango-Russian_schoolhouse_transcription',
    'hellerick-C17A': r'/home/hellerick/PycharmProjects/Ango-Russian_schoolhouse_transcription'
}[platform.node()]


English_alphabet = 'abcdefghijklmnopqrstuvwxyzëéï'


def translit_cyr(word):
    translit_pairs=[
        ['ce', 'се'], ['ci', 'си'], ['cy', 'си'], ['ya', 'ья'], ['ye', 'ье'],
        ['yi', 'ьи'], ['yo', 'ьо'], ['yu', 'ью'], ['ch', 'ч'], ['sh', 'ш'],
        ['th', 'т'], ['a', 'ф'], ['b', 'б'], ['c', 'к'], ['d', 'д'],
        ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'и'],
        ['j', 'дж'], ['k', 'к'], ['l', 'л'], ['m', 'м'], ['n', 'н'],
        ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'],
        ['u', 'у'], ['v', 'в'], ['w', 'ў'], ['x', 'кс'], ['y', 'и'], ['z', 'з']
    ]
    for pair in translit_pairs:
        word = word.replace(*pair)
    word = re.sub(r'(\A|[аеиоуяю])ь', r'\1', word)
    word = re.sub(r'(\A|[аеиоуяю])е', r'\1э', word)
    return word


def try_lat_phonet_matching(prev_cyr, next_lat, next_phonet, rules):
    print(prev_cyr, next_lat, next_phonet)
    if next_lat=='' and next_phonet==[]:
        return prev_cyr
    else:
        for rule in rules:
            if re.match(rule[0], next_lat) and re.fullmatch(rule[1], next_phonet[0]):
                try_lat_phonet_matching(prev_cyr+rule[2], next_lat[re.match(rule[0], next_lat).span()[0]:], next_phonet[1:], rules)


def phonet_cyr(lat, phonet, rules=[]):
    cyr = try_lat_phonet_matching(prev_cyr='', next_lat=lat, next_phonet=phonet.split(), rules=rules)
    return cyr


def convert_text(text):
    # make-wordlist
    # convert by user dictionary
    # make dictionary based on US, then on UK dictionary; convert
    # try convert by word-breaking
    pass


def make_local_dictionary(file_path, word_list):
    local_dict_path = re.sub(r'\.[a-z]+\Z', '.Dictionary.txt', file_path)
    user_dict_path = os.path.join(project_path, 'Dictionaries', 'User_dict.txt')
    US_dict_path = os.path.join(project_path, 'Dictionaries', 'cmudict.0.7a')
    UK_dict_path = os.path.join(project_path, 'Dictionaries', 'beep-1.0')

    rules_path = os.path.join(project_path, 'Transcription_rules.txt')
    with open(rules_path, mode='rt', encoding='utf8') as f:
        rules =  f.read()

    rules = re.sub(r'#.*?\n', r'\n', rules)
    rules = rules.split('\n')
    rules = [re.sub(r'(.*)#.*', r'\1', line) for line in rules]
    rules = [line for line in rules if line != '']
    rules = [re.split(r' ?= ?', line) for line in rules]
    for r in rules:
        if r[1] == '-': r[1] = ''
    for r in rules:
        if r[2] == '-': r[2] = ''
    rules.sort(key = lambda x: len(x[0]), reverse=True)
    # for r in rules: print(r)

    with open(user_dict_path, mode='rt', encoding='utf8') as f:
        user_dict =  f.read()
    user_dict = re.sub(r'  +', r' ', user_dict)
    user_dict = re.sub(r'#.*?\n', r'\n', user_dict)
    user_dict = user_dict.split('\n')
    user_dict = [re.sub(r'(.*)#.*', r'\1', line) for line in user_dict]
    user_dict = [line for line in user_dict if line != '']
    user_dict = [re.split(r' ?= ?', line) for line in user_dict]
    user_dict = {line[0]:line[1] for line in user_dict}
    # print(user_dict)

    with open(US_dict_path, mode='rt', encoding='utf8') as f:
        US_dict =  f.read()
    US_dict = re.sub(r';.*?\n', r'\n', US_dict)
    US_dict = re.sub(r'\(1\)', r'', US_dict)
    US_dict = re.sub(r"'", r'’', US_dict)
    US_dict = US_dict.split('\n')
    # US_dict = [re.sub(r'(.*);.*', r'\1', line) for line in US_dict]
    US_dict = [line for line in US_dict if line != '']
    US_dict = [re.split(r'  ', line) for line in US_dict]
    US_dict = {line[0].lower():line[1] for line in US_dict}
    # print(US_dict)

    with open(UK_dict_path, mode='rt', encoding='utf8') as f:
        UK_dict =  f.read()
    UK_dict = re.sub(r'#.*?\n', r'\n', UK_dict)
    UK_dict = re.sub(r'\(1\)', r'', UK_dict)
    UK_dict = re.sub(r"'", r'’', UK_dict)
    UK_dict = UK_dict.split('\n')
    # UK_dict = [re.sub(r'(.*)#.*', r'\1', line) for line in UK_dict]
    UK_dict = [line for line in UK_dict if line != '']
    UK_dict = [re.split(r'\s+', line) for line in UK_dict]
    UK_dict = {line[0].lower():' '.join(line[1:]).upper() for line in UK_dict}
    print(UK_dict)

    phonet_dict = dict()
    for word in word_list:
        if word in US_dict:
            phonet_dict[word] = US_dict[word]
        elif word in UK_dict:
            phonet_dict[word] = UK_dict[word]

    cyr_dict = dict()
    for word in word_list:
        if word in phonet_dict:
            cyr_dict[word] = phonet_cyr(word, phonet_dict[word], rules)
        else:
            cyr_dict[word] = translit_cyr(word)


def convert_file(file_path):
    with open(file_path, mode='rt', encoding='utf8') as f:
        code = f.read()
    code = re.split('(<[^>]+>)', code)
    # print(code[:50])
    word_list = list()
    for n, text in enumerate(code):
        if n%2 == 0:
            local_list = re.findall('['+English_alphabet+'’]*['+English_alphabet+']', text.lower())
            word_list += local_list
    word_list = sorted(list(set(word_list)))
    word_list_path = re.sub(r'\.[a-z]+\Z', '.WordList.txt', file_path)
    with open(word_list_path, 'wt', encoding='utf8') as word_list_file:
        word_list_file.write('\n'.join(word_list))
    make_local_dictionary(file_path, word_list)
    for n, text in enumerate(code):
        if n%2 == 0:
            code[n] = convert_text(text)
    # print(code[:50])


def main():

    file_path = os.path.join(
        project_path, 'Examples',
        'Eoin Colfer. Artemis Fowl 01.html'
    )

    convert_file(file_path)


if __name__ == '__main__':
    main()