import os
import platform
import re
import pickle

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
        ['yi', 'ьи'], ['yo', 'ьо'], ['yu', 'ью'], ['ch', 'ч'], 
        ['sh', 'ш'], ['th', 'т'], ['a', 'а'], ['b', 'б'], ['c', 'к'],
        ['d', 'д'], ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'и'],
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
    global watch
    watch += f'\n - {prev_cyr}, {next_lat}, {repr(next_phonet)}'
    if next_lat=='' and next_phonet==[]:
        # print(f' : {prev_cyr}')
        return prev_cyr
    else:
        for rule in rules:
            if re.match(rule[0], next_lat) and re.match(rule[1], ' '.join(next_phonet)):
                # print('   rule:', rule)
                if rule[1]=='':
                    phonet_len = 0
                else:
                    phonet_len = len(re.match(rule[1], ' '.join(next_phonet)).group().split())
                attempt = try_lat_phonet_matching(
                    prev_cyr+rule[2],
                    next_lat[re.match(rule[0], next_lat).span()[1]:],
                    next_phonet[phonet_len:],
                    rules
                )
                if attempt: return attempt


def phonet_cyr(lat, phonet, rules=[]):
    global watch
    watch = f'{lat} [{phonet}]'
    cyr = try_lat_phonet_matching(prev_cyr='', next_lat=lat, next_phonet=phonet.split(), rules=rules)
    if cyr == None:
        print(watch)
        raise Exception('Not matched!')
    return cyr


def convert_word(word, cyr_dict):
    if word == '':
        return word
    if word[0].isupper():
        if len(word)<2 or word[1].islower():
            case = 'title'
        else:
            case = 'allcaps'
    else:
        case = 'lower'
    word = cyr_dict[word.lower()]
    if case == 'title':
        word = word[0].upper() + word[1:]
    elif case == 'allcaps':
        word = word.upper()
    return word


def convert_text(text, cyr_dict):
    text = re.sub(r'(['+English_alphabet+r']\s)I', r'\1i', text)
    text = re.split('(['+English_alphabet+English_alphabet.upper()+'’]*['+English_alphabet+English_alphabet.upper()+'])', text)
    #print(f'Text <{text}>')
    for n, word in enumerate(text):
        if n%2 == 1:
            text[n] = convert_word(word, cyr_dict)
    return ''.join(text)


def try_breaking(word, cyr_dict):
    boundary = sorted(list(range(1, len(word))), key = lambda x: abs(x - len(word)/2))
    for b in boundary:
        if word[:b] in cyr_dict and word[b:] in cyr_dict:
            print(f'Word broken: {word[:b]} + {word[b:]}')
            return cyr_dict[word[:b]]+cyr_dict[word[b:]]


def postprocess(cyr_dict, user_dict, full_normalization = False):
    lat_words = cyr_dict.keys()
    cyr_words = '\n'.join(cyr_dict.values())
    rules = [
        [r'(\b|-|а|е|о|у|ў|ю|́)е', r'\1э̀'],
        [r'(\b|-|а|е|о|у|ў|ю|́)ё', r'\1ӭ'],
        [r'ьйа','ья'],
        [r'ьйу', 'ью'],
        [r'\bьйе', 'йе'],
        [r'ьйе', 'ье'],
        [r'(\b|а|е|и|о|у|ю|́)ь', r'\1'],
        ['э̀й', 'эй'],
        [r'([бгдзлмнпрстф])\1([бдзклмнпртсф])', r'\1\2'],
        [r'([гзлрстф])\1\b', r'\1'],
    ]
    if full_normalization:
        rules = rules + [
            ['ўу', 'ву'],
            ['ў', 'у'],
            ['(т̈|д̈|ҙ|ҫ)', 'т'],
            ['[̈́̀]', ''],
        ]
    for rule in rules:
        cyr_words = re.sub(rule[0], rule[1], cyr_words)
    cyr_dict = dict(zip(lat_words, cyr_words.split('\n')))
    for word in user_dict:
        cyr_dict[word] = user_dict[word]
    return cyr_dict


def dialog_mode(cyr_dict):
    while True:
        u = input()
        try:
            print(cyr_dict[u.lower()])
        except KeyError:
            pass
        if u == '':
            return None


def make_local_dictionary(file_path, word_list):
    local_dict_path = re.sub(r'\.[a-z]+\Z', '.Dictionary.txt', file_path)
    user_dict_path = os.path.join(project_path, 'Dictionaries', 'User_dict.txt')
    US_dict_path = os.path.join(project_path, 'Dictionaries', 'cmudict.0.7a')
    UK_dict_path = os.path.join(project_path, 'Dictionaries', 'beep-1.0')
    local_dict_path = os.path.join(project_path, 'Dictionaries', 'Local_dict.txt')
    local_dict_pickle_path = os.path.join(project_path, 'Dictionaries', 'Local_dict.pickle')

    if os.path.exists(local_dict_pickle_path):
        return pickle.load(open(local_dict_pickle_path, mode='rb'))

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
    rules.sort(key = lambda x: len(x[1]), reverse=True)
    rules.sort(key = lambda x: len(x[0]), reverse=True)
    rules.sort(key = lambda x: x[1]=='')
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
    # US_dict = re.sub(r'\(1\)', r'', US_dict)
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
    # print(UK_dict)

    phonet_dict = dict()
    for word in word_list:
        if word in US_dict:
            phonet_dict[word] = US_dict[word]
        elif word in UK_dict:
            phonet_dict[word] = UK_dict[word]

    cyr_dict = {word:user_dict[word] for word in user_dict}
    for word in word_list:
        if not word in user_dict and word in phonet_dict:
            cyr_dict[word] = phonet_cyr(word, phonet_dict[word], rules)
    for word in word_list:
        if not word in cyr_dict:
            attempt = try_breaking(word, cyr_dict)
            if attempt:
                cyr_dict[word] = attempt
            else:
                print('Not found:', word)
                cyr_dict[word] = translit_cyr(word)
    cyr_dict = postprocess(cyr_dict, user_dict, full_normalization=False)

    cyr_list = sorted([word+' = '+cyr_dict[word] for word in cyr_dict])
    cyr_list = '\n'.join(cyr_list)
    with open(local_dict_path, mode='wt', encoding='utf8') as f:
        f.write(cyr_list)

    pickle.dump(cyr_dict, open(local_dict_pickle_path, mode='wb'))

    return cyr_dict


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
    cyr_dict = make_local_dictionary(file_path, word_list)
    for n, text in enumerate(code):
        if n%2 == 0:
            code[n] = convert_text(text, cyr_dict)
    code = ''.join(code)
    output_path = re.sub(r'(.*)\.([a-zA-Z0-9]+)', r'\1.Cyr.\2', file_path)
    with open(output_path, mode='wt', encoding='utf8') as f:
        f.write(code)


def main():

    file_path = os.path.join(
        project_path, 'Examples',
        'Eoin Colfer. Artemis Fowl 01.html'
    )

    convert_file(file_path)


if __name__ == '__main__':
    main()