# coding=utf-8
import os
import platform
import re
import pickle


project_path = {
    'DESKTOP-62BVD4A': 'd:\KPV\Github\English_Cyrillic_script',
    'hellerick-C17A': '/home/hellerick/PycharmProjects/English_Cyrillic_script',
    'Superkomp': 'D:\HCF\PyCharmProjects\English_Cyrillic_script',
}[platform.node()]

Hellerick_2015 = 'H15'
Schoolhouse = 'SCH'
Cyrillic_English_Socialist_Alphabet = 'CISA'
Latin_English_Socialist_Alphabet = 'LISA'
Gothic_English_Alphabet = 'GOTH'
Thornica = "THOR"
Penderscript = "PEND"
Latin_English_Reformed_Alphabet = "LIRA"
Cyrillic_English_Reformed_Alphabet = 'CIRA'


system = 'CIRA'

English_alphabet = 'abcdefghijklmnopqrstuvwxyzáàâāäçéëêèíïñōöôúūſæœ'

hyphenate = False


def translit_cyr(word):
    if system == 'H15':
        translit_pairs = [
            ['ce', 'се'], ['ci', 'сі'], ['cy', 'сі'], ['ya', 'іа'], ['ye', 'іе'],
            ['yi', 'іі'], ['yo', 'іо'], ['yu', 'ю'], ['ch', 'ч'],
            ['sh', 'ш'], ['th', 'ѳ'],
            ['a', 'а'], ['b', 'б'], ['c', 'к'],
            ['d', 'д'], ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'і'],
            ['j', 'џ'], ['k', 'к'], ['l', 'л'], ['m', 'м'], ['n', 'н'],
            ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'],
            ['u', 'у'], ['v', 'в'], ['w', 'ѵ'], ['x', 'кс'], ['y', 'і'], ['z', 'з'],
            ['á', 'а́'], ['ā', 'а́'],  ['ō', 'о́'], ['ū', 'у́'], 
        ]
    elif system == 'SCH':
        translit_pairs = [
            ['ce', 'се'], ['ci', 'си'], ['cy', 'си'], ['ya', 'ья'], ['ye', 'ье'],
            ['yi', 'ьи'], ['yo', 'ьо'], ['yu', 'ью'], ['ch', 'ч'],
            ['sh', 'ш'], ['th', 'т'],
            ['yá', 'ья́'],
            ['a', 'а'], ['b', 'б'], ['c', 'к'],
            ['d', 'д'], ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'и'],
            ['j', 'дж'], ['k', 'к'], ['l', 'л'], ['m', 'м'], ['n', 'н'],
            ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'],
            ['u', 'у'], ['v', 'в'], ['w', 'ў'], ['x', 'кс'], ['y', 'и'], ['z', 'з'],
            ['á', 'а́']
        ]
    elif system == 'CISA':
        translit_pairs = [
            ['ce', 'се'], ['ci', 'си'], ['cy', 'си'], ['ya', 'ја'], ['ye', 'је'],
            ['yi', 'ји'], ['yo', 'јо'], ['yu', 'ју'], ['ch', 'ч'],
            ['sh', 'ш'], ['th', 'ꚋ'], ['wh', 'ү'],
            ['yá', 'ја́'],
            ['a', 'а'], ['b', 'б'], ['c', 'к'],
            ['d', 'д'], ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'и'],
            ['j', 'ж'], ['k', 'к'], ['l', 'л'], ['m', 'м'], ['n', 'н'],
            ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'],
            ['u', 'у'], ['v', 'в'], ['w', 'ү'], ['x', 'кс'], ['y', 'и'], ['z', 'з'],
            ['á', 'а́'], ['ū', 'у́']
        ]
    elif system == 'CIRA':
        translit_pairs = [
            ['tch', 'ч'], 
            ['ce', 'це'], ['ci', 'ці'], ['cy', 'сі'], ['ya', 'ја'], ['ye', 'је'],
            ['yi', 'јі'], ['yo', 'јо'], ['yu', 'ју'], ['ch', 'ч'],
            ['sh', 'ш'], ['th', 'þ'], ['wh', 'у'],
            ['yá', 'ја́'],
            ['a', 'а'], ['b', 'б'], ['c', 'к'],
            ['d', 'д'], ['e', 'е'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'і'],
            ['j', 'ж'], ['k', 'к'], ['l', 'л'], ['m', 'м'], ['n', 'н'],
            ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'],
            ['u', 'у'], ['v', 'в'], ['w', 'у'], ['x', 'кс'], ['y', 'і'], ['z', 'з'],
            ['á', 'а́'], ['ū', 'у́'], ['ñ', 'нj'],
        ]
    elif system == 'LISA':
        translit_pairs = [
            ['ce', 'ce'], ['ci', 'ci'], ['cy', 'ci'], ['ya', 'ya'], ['ye', 'ye'],
            ['yi', 'yi'], ['yo', 'yo'], ['yu', 'yu'], ['ch', 'ch'],
            ['sh', 'sh'], ['th', 'th'], ['wh', 'w'],
            ['yá', 'yа́'],
            ['a', 'a'], ['b', 'b'], ['c', 'k'],
            ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'],
            ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'],
            ['o', 'o'], ['p', 'p'], ['q', 'k'], ['r', 'r'], ['s', 's'], ['t', 't'],
            ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'i'], ['z', 'z'],
            ['á', 'á']
        ]
    elif system == 'LIRA' or system == 'LIRA2':
        translit_pairs = [
            ['ce', 'ce'], ['ci', 'ci'], ['cy', 'ci'], ['ya', 'ya'], ['ye', 'ye'],
            ['yi', 'yi'], ['yo', 'yo'], ['yu', 'yu'], ['ch', 'ch'],
            ['sh', 'sh'], ['th', 'th'], ['wh', 'w'],
            ['yá', 'yа́'],
            ['a', 'a'], ['b', 'b'], ['c', 'k'],
            ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'],
            ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'],
            ['o', 'o'], ['p', 'p'], ['q', 'k'], ['r', 'r'], ['s', 's'], ['t', 't'],
            ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'i'], ['z', 'z'],
            ['á', 'á'],
        ]
    elif system == 'GOTH':
        translit_pairs = [ # 𐌰 𐌰̈ 𐌱 𐌲 𐌲̈ 𐌳 𐌴 𐌴̈ 𐌶 𐌷 𐌸 𐌹 𐌹̈ 𐌺 𐌺̈ 𐌻 𐌼 𐌽 𐌾 𐌿 𐌿̈ 𐍀 𐍁 𐍂 𐍃 𐍃̈ 𐍄 𐍅 𐍅̈ 𐍆 𐍇 𐍈 𐍉 𐍉̈
            ['ce', '𐍇𐌴'], ['ci', '𐍇𐌹'], ['cy', '𐍇𐌹'], ['ya', '𐌾𐌰'], ['ye', '𐌾𐌴'],
            ['yi', '𐌾𐌹'], ['yo', '𐌾𐍉'], ['yu', '𐌾𐌿'], ['ch', '𐌺̈'],
            ['sh', '𐍃̈'], ['th', '𐌸'], ['wh', '𐍈'],
            ['yá', '𐌾𐌰'],
            ['a', '𐌰'], ['b', '𐌱'], ['c', '𐌺'],
            ['d', '𐌳'], ['e', '𐌴'], ['f', '𐍆'], ['g', '𐌲'], ['h', '𐌷'], ['i', '𐌹'],
            ['j', '𐌲̈'], ['k', '𐌺'], ['l', '𐌻'], ['m', '𐌼'], ['n', '𐌽'],
            ['o', '𐍉'], ['p', '𐍀'], ['q', '𐌺'], ['r', '𐍂'], ['s', '𐍃'], ['t', '𐍄'],
            ['u', '𐌿'], ['v', '𐍅̈'], ['w', '𐍅'], ['x', '𐌺𐍃'], ['y', '𐌹'], ['z', '𐌶'],
            ['á', '𐌰']
        ]
    elif system == 'ANG':
        translit_pairs = [ # ç ó þ
            ['ce', 'çe'], ['ci', 'çi'], ['cy', 'çi'], ['ya', 'gea'], ['ye', 'ge'],
            ['yi', 'gi'], ['yo', 'geo'], ['yu', 'geu'], ['ch', 'c'],
            ['sh', 'sc'], ['th', 'þ'], ['wh', 'hw'],
            ['yá', 'geа́'],
            ['ke', 'ché'], ['ki', 'chí'],
            ['a', 'a'], ['b', 'b'], ['c', 'c'],
            ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'],
            ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'],
            ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'],
            ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'i'], ['z', 'z'],
            ['á', 'á']
        ]
    elif system == 'THOR':
        translit_pairs = [ # þ ú
            ['th', 'þ'],
            ['a', 'a'], ['b', 'b'], ['c', 'c'],
            ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'],
            ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'],
            ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'],
            ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'i'], ['z', 'z'],
            ['á', 'á'], ['é', 'é']
        ]
    elif system == 'PEND':
        translit_pairs = [ # þ ú
            ['th', 'th'],
            ['a', 'a'], ['b', 'b'], ['c', 'c'],
            ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'],
            ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'],
            ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'],
            ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'i'], ['z', 'z'],
            ['á', 'á'], ['é', 'é']
        ]
    for pair in translit_pairs:
        word = word.replace(*pair)
    word = re.sub(r'(\A|[аеиоуяю])ь', r'\1', word)
    if system == 'SCH':
        word = re.sub(r'(\A|[аеиоуяю])е', r'\1э', word)
    return word


def try_lat_phonet_matching(prev_cyr, next_lat, next_phonet, rules):
    global watch
    watch += f'\n - {prev_cyr}, {next_lat}, {repr(next_phonet)}'
    if next_lat == '' and next_phonet == []:
        # print(f' : {prev_cyr}')
        return prev_cyr
    else:
        for rule in rules:
            if re.match(rule[0], next_lat) and re.match(rule[1], ' '.join(next_phonet)):
                # print('   rule:', rule)
                if rule[1] == '':
                    phonet_len = 0
                else:
                    phonet_len = len(re.match(rule[1], ' '.join(next_phonet)).group().split())
                attempt = try_lat_phonet_matching(
                    prev_cyr + rule[2],
                    next_lat[re.match(rule[0], next_lat).span()[1]:],
                    next_phonet[phonet_len:],
                    rules
                )
                if attempt:
                    #print(rule)
                    return attempt


def phonet_cyr(lat, phonet, rules=[]):
    global watch
    watch = f'{lat} [{phonet}]'
    cyr = try_lat_phonet_matching(prev_cyr='', next_lat='<'+lat+'>', next_phonet=phonet.split(), rules=rules) # the characters '<' and '>' would stand fro start/end of the word
    if cyr == None:
        print(watch)
        print('==Exception: Not matched!==')
        #raise Exception('Not matched!')
##    print('phonet_cyr', lat, '=', cyr)
    return cyr


def convert_word(word, cyr_dict):
    if word == '':
        return word
    if word[0].isupper():
        if len(word) < 2 or word[1].islower() or word[1] in ['’']:
            case = 'title'
        else:
            case = 'allcaps'
    elif word[0] == '’' and word[1].isupper():
        if len(word) < 3 or word[2].islower():
            case = 'apo-title'
        else:
            case = 'allcaps'
    else:
        case = 'lower'
    word = cyr_dict[word.lower()]
    if case == 'title':
        word = word[0].upper() + word[1:]
    elif case == 'apo-title':
        word = word[0] + word[1].upper() + word[2:]
    elif case == 'allcaps':
        word = word.upper()
    # print('convert_word', word)
    return word


def convert_text(text, cyr_dict):
    if not system=='PEND':
        text = re.sub(r'([' + English_alphabet + r',]\s)I\b', r'\1i', text)
##    text = re.sub(r'([A-Z])([A-Z][a-z])', r'\1`=`\2', text)
    text = re.split(
        '([' + English_alphabet + English_alphabet.upper() + '’]*[' + English_alphabet + English_alphabet.upper() + '][0-9]?)',
        text)
    # print(f'Text <{text}>')
    for n, word in enumerate(text):
        if n % 2 == 1:
            text[n] = convert_word(word, cyr_dict)
    text = ''.join(text)
##    text = re.sub('`=`', r'', text)
    return text


def try_breaking(word, cyr_dict, phonet_dict, rules):
    boundary = sorted(list(range(1, len(word))), key=lambda x: abs(x - len(word) / 2))
    for b in boundary:
        if (word[:b] in cyr_dict or word[:b] in phonet_dict) and (word[b:] in cyr_dict or word[b:] in phonet_dict):
            print(f'Word broken: {word[:b]} + {word[b:]}')
            returned = [cyr_dict[w] if w in cyr_dict else phonet_cyr(w, phonet_dict[w], rules) for w in
                        [word[:b], word[b:]]]
            try:
                return '¬'.join(returned)
            except Exception:
                return 'None'


def postprocess(cyr_dict, user_dict, full_normalization=False):
    lat_words = cyr_dict.keys()
    cyr_words = '\n'.join(cyr_dict.values())  # т̈
    rules = [
        [r'(\b|-|а|е|о|у|ў|ю|́)е', r'\1э̀'],
        [r'(\b|-|а|е|о|у|ў|ю|́)ё', r'\1ӭ'],
        [r'ьйа', 'ья'],
        [r'ьйу', 'ью'],
        [r'\bьйе', 'йе'],
        [r'ьйе', 'ье'],
        [r'(\b|а|е|и|о|у|ю|́)ь', r'\1'],
        ['э̀й', 'эй'],
        [r'([бгдзлмнпрстф])\1([бдзклмнпртсф])', r'\1\2'],
        [r'([гзклмрстф])\1(\b|ь)', r'\1\2'],
        [r'ўу', 'в̆у'],
    ]
    if full_normalization:
        rules = rules + [
            ['̆в', 'в'],
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
    missing_words = list()
    local_dict_path = re.sub(r'\.[a-z]+\Z', '.Dictionary.txt', file_path)
    user_dict_path = os.path.join(project_path, 'Dictionaries', 'User_dict.' + system + '.txt')
    US_dict_path = os.path.join(project_path, 'Dictionaries', 'cmudict.0.7a')
    UK_dict_path = os.path.join(project_path, 'Dictionaries', 'beep-1.0')
    local_dict_path = os.path.join(project_path, 'Dictionaries', 'Local_dict.txt')
    local_dict_pickle_path = os.path.join(project_path, 'Local_dict.pickle')
    missing_dict_path = os.path.join(project_path, 'Missing_word_list.txt')

    if os.path.exists(local_dict_pickle_path):
        return pickle.load(open(local_dict_pickle_path, mode='rb'))

    rules_path = os.path.join(project_path, 'Transcription_rules.' + system + '.txt')
    with open(rules_path, mode='rt', encoding='utf8') as f:
        rules = f.read()

    rules = re.sub(r'#.*?\n', r'\n', rules)
    rules = rules.split('\n')
    rules = [re.sub(r'(.*)#.*', r'\1', line) for line in rules]
    rules = [line for line in rules if line != '']
    rules = [re.split(r' ?= ?', line) for line in rules]
    rules = rules + [['<','-','-'], ['>','-','-']] # Adding ability to ignore the word-initial/final characters '<' and '>'.
    for r in rules:
        if r[1] == '-': r[1] = ''
    for r in rules:
        if r[2] == '-': r[2] = ''
    rules.sort(key=lambda x: len(x[1]), reverse=True)
    rules.sort(key=lambda x: len(x[0]), reverse=True)
    rules.sort(key=lambda x: x[1] == '')
    # for r in rules: print(r)

    with open(user_dict_path, mode='rt', encoding='utf8') as f:
        user_dict = f.read()
    user_dict = re.sub(r'  +', r' ', user_dict)
    user_dict = re.sub(r'#.*?\n', r'\n', user_dict)
    user_dict = re.sub(r' ?\n ?', r'\n', user_dict)
    user_dict = user_dict.split('\n')
    user_dict = [re.sub(r'(.*)#.*', r'\1', line) for line in user_dict]
    user_dict = [line for line in user_dict if line != '']
    user_dict = [re.split(r' ?= ?', line) for line in user_dict]
    user_dict = {line[0]: line[1] for line in user_dict}
    # print(user_dict)

    with open(US_dict_path, mode='rt', encoding='utf8') as f:
        US_dict = f.read()
    US_dict = re.sub(r';.*?\n', r'\n', US_dict)
    # US_dict = re.sub(r'\(1\)', r'', US_dict)
    US_dict = re.sub(r"'", r'’', US_dict)
    US_dict = US_dict.split('\n')
    # US_dict = [re.sub(r'(.*);.*', r'\1', line) for line in US_dict]
    US_dict = [line for line in US_dict if line != '']
    US_dict = [re.split(r'  ', line) for line in US_dict]
    US_dict = {line[0].lower(): line[1] for line in US_dict}
    # print(US_dict)

    with open(UK_dict_path, mode='rt', encoding='utf8') as f:
        UK_dict = f.read()
    UK_dict = re.sub(r'#.*?\n', r'\n', UK_dict)
    UK_dict = re.sub(r'\(1\)', r'', UK_dict)
    UK_dict = re.sub(r"'", r'’', UK_dict)
    UK_dict = UK_dict.split('\n')
    # UK_dict = [re.sub(r'(.*)#.*', r'\1', line) for line in UK_dict]
    UK_dict = [line for line in UK_dict if line != '']
    UK_dict = [re.split(r'\s+', line) for line in UK_dict]
    UK_dict = {line[0].lower(): ' '.join(line[1:]).upper() for line in UK_dict}
    # print(UK_dict)

    phonet_dict = dict()
    # for word in word_list:
    #     if word in US_dict:
    #         phonet_dict[word] = US_dict[word]
    #     elif word in UK_dict:
    #         phonet_dict[word] = UK_dict[word]
    for word in US_dict:
        phonet_dict[word] = US_dict[word]
    for word in UK_dict:
        if not word in phonet_dict:
            phonet_dict[word] = UK_dict[word]

    cyr_dict = {word: user_dict[word] for word in user_dict}
    cyr_list = ''
    for word in word_list:
        if not word in user_dict and word in phonet_dict:
            cyr_dict[word] = phonet_cyr(word, phonet_dict[word], rules)
            print(word, '=', cyr_dict[word])
            try:
                cyr_list = cyr_list + word + ' = ' + cyr_dict[word] + ' # ' + phonet_dict[word] + '\n'
            except Exception:
                pass
    for word in word_list:
        if not word in cyr_dict:
            attempt = try_breaking(word, cyr_dict, phonet_dict, rules)
            if attempt:
                cyr_dict[word] = attempt
            else:
                print('Not found:', word)
                cyr_dict[word] = translit_cyr(word)
                missing_words = missing_words + [word]
    if system == 'SCH':
        cyr_dict = postprocess(cyr_dict, user_dict, full_normalization=False)

    with open(local_dict_path, mode='wt', encoding='utf8') as f:
        f.write(cyr_list)

    if system in ['H15', 'SCH', 'CISA', 'CIRA']:
        cyr_dict = eval(hyphenate_code(repr(cyr_dict)))
    elif system in ['LISA', 'ANG', 'LIRA', 'LIRA2', 'PEND']:
        in_dict = [word for word in cyr_dict]
        out_dict = [cyr_dict[word] for word in cyr_dict]
        out_dict = eval(hyphenate_code(repr(out_dict)))
        cyr_dict = zip(in_dict, out_dict)
        cyr_dict = {pair[0]:pair[1] for pair in cyr_dict}
##        print('make_local_dictionary', cyr_dict)

    if not 'default.txt' in file_path:
        pickle.dump(cyr_dict, open(local_dict_pickle_path, mode='wb'))

    with open(missing_dict_path, mode='wt', encoding='utf8') as f:
        f.write('\n'.join(sorted(missing_words)))

    return cyr_dict


def hyphenate_code(code):
    # ¬
    if hyphenate and system in ('H15', 'SCH', 'CISA', 'CIRA'):
        vow = 'аӕеёәєиіоөѵуұъыэюяѵѡ'
        dia = '́̀̈'
        con = 'бвв̆гджзҙӡѕйјклмнпрсҫтꚋþўфхцчшщѵүѳџ'
        if system == "H15":
            con = con + 'і'
        if system == "CIRA":
            con = con + 'у'
        trucon = re.sub('[іѵүу]', '', con)
        let = vow + dia + con + 'ь'
        vow, dia, con, let, trucon = [f'[{x}]' for x in [vow, dia, con, let, trucon]]
        code = re.sub(r'(' + let + '+)', r'<<\1>>', code)
        code = re.sub(r'(' + con + 'ь?' + vow + ')', r'¬\1', code)
        code = re.sub(r'в¬̆', r'¬в̆', code)
        code = re.sub(r'(' + vow + '|' + dia + ')(' + vow + ')', r'\1¬\2', code)
        code = re.sub(r'(' + vow + ')¬й', r'\1й¬', code)
        code = re.sub(r'(' + vow + ')¬й', r'\1й¬', code)
        code = re.sub(r'(а|о)¬у', r'\1у', code)
        for c in ['дж', 'жў'] or (c in ['іу'] and system == 'H15'):
            code = re.sub(c[0] + '¬' + c[1], '¬' + c, code)
        for c in ['еі', 'еѵ', 'аі', 'аѵ', 'оі', 'оѵ', 'ѵе', 'ѵі', 'ѵо', 'іа', 'іѵ']:
            code = re.sub(c[0] + '¬' + c[1], c, code)
        if system == 'CISA':
            code = re.sub(r'([аео])¬и', r'\1и', code)
        code = re.sub(r'¬([лмнр])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'¬([лмнр])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'¬(' + con + r')\1', r'\1¬\1', code)
        code = re.sub(r'¬([лмнр])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'([бгдкптф])¬([лр])', r'¬\1\2', code)
        code = re.sub(r'¬([дт])л', r'\1¬л', code)
        code = re.sub(r'нс¬ц', r'н¬сц', code)
        code = re.sub(r'н¬гл', r'нг¬л', code)
        code = re.sub(r'([бгдкмпрт])¬?с¬([птк])', r'\1¬с\2', code)
        code = re.sub(r'¬(' + con + ')ли>>', r'\1¬ли', code)
        code = re.sub(r'([аеиоуӕєіөұ])¬([бвгджзјклмнпрстþфхцчш])¬?([бвгджзјклмнпрстþфхцчш])', r'\1\2¬\3', code)
        if system == 'CIRA':
            code = re.sub(r'¬(' + con + '+ес>>)', r'\1', code)
            code = re.sub(r'('+vow + r')¬ес>>', r'\1ес', code)
            code = re.sub(r'('+vow + r')¬ед>>', r'\1ед', code)
            code = re.sub(r'¬([бвгѕзјклмнпрсþуфцчш]ед>>)', r'\1', code)
            code = re.sub(r'<<ѵн([с])¬', r'<<ѵн¬\1', code)
            code = re.sub(r'у¬([аӕеєіиоөуұѵ])', r'¬у\1', code)
            code = re.sub(r'<<ек¬с([бвгджзјклмнпрстþфхцчш])', r'екс¬\1', code)
            code = re.sub(r'¬?([бвгджзјклмнпрстþфхцчш])¬у¬?([аӕеєіиоөуұѵ])', r'\1¬у\2', code)
            code = re.sub(r'([зстц])і¬([аео])', r'\1і\2', code)
            code = re.sub(r'о¬у(інг|ер|ес)>>', r'оу¬\1>>', code)
            code = re.sub(r'([ао])¬уе', r'\1у¬е', code)
            code = re.sub(r'([аео])¬јі', r'\1ј¬і', code)
        code = re.sub(r'<<¬?(де|ре)([бдкптк])¬([лр])', r'<<\1¬\2\3', code)
        code = re.sub(r'<<(.)>>¬<<¬*', r'<<\1', code)
        code = re.sub(r'¬(' + con + '+¬>>)', r'\1', code)
        code = re.sub(r'¬>>', r'>>', code)
        code = re.sub(r'<<¬+', r'<<', code)
        code = re.sub(r'¬(' + vow + dia + '?)>>', r'\1>>', code)
        code = re.sub(r'<<(' + trucon + '+' + dia + '?|' + vow + dia + '?)¬', r'<<\1', code)
        code = re.sub(r'<<(' + trucon + '+' + dia + '?|' + vow + dia + '?)¬', r'<<\1', code)
        code = re.sub(r'(<<|>>)', r'', code)
        code = re.sub(r'¬¬', r'¬', code)
        code = re.sub(r'¬', r'­', code)
    elif hyphenate and system in ('LISA', 'ANG', 'LIRA', 'LIRA2', 'PEND'):
        vow = 'aeiouyəäëïöüáéíôóûú'
        dia = '́̀̈'
        con = 'bcdfghjklmnpqrstvwxyz'
        trucon = re.sub('[y]', '', con)
        let = vow + dia + con
        vow, dia, con, let, trucon = [f'[{x}]' for x in [vow, dia, con, let, trucon]]
        code = re.sub(r'(' + let + '+)', r'<<\1>>', code)
        code = re.sub(r'(' + con + vow + ')', r'¬\1', code)
        code = re.sub(r'(' + vow + '|' + dia + ')(' + vow + ')', r'\1¬\2', code)
        code = re.sub(r'(' + vow + '|' + dia + ')(' + vow + ')', r'\1¬\2', code)
        code = re.sub(r'(a|e|o)¬(i|u)', r'\1\2', code)
        for c in ['ch', 'sh', 'th', 'wh']:
            code = re.sub(c[0] + '¬' + c[1], '¬' + c, code)
        for c in ['ei', 'ai', 'ay', 'au', 'aú', 'ey', 'oi', 'oo', 'ou', 'uu', 'ya', 'yä', 'ye', 'yë', 'yi', 'yï', 'yo', 'yö', 'yu', 'yü', 'yə', 'əi', 'əu']:
            code = re.sub(c[0] + '¬' + c[1], c, code)
        code = re.sub(r'¬([lmnr])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'¬(' + con + r')\1', r'\1¬\1', code)
        code = re.sub(r'¬([lmnr])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'([bdfgkpt])¬([r])', r'¬\1\2', code)
        code = re.sub(r'([bdfgkpt])¬([l])', r'¬\1\2', code)
        code = re.sub(r'¬([dt])([l])', r'\1¬\2', code)
        code = re.sub(r'(ci|di|qu|si|ti|zi)¬('+vow+')', r'\1\2', code)
        code = re.sub(r'([bdfgjklmnprtvz])¬?s¬([ptk])', r'\1¬s\2', code)
        code = re.sub(r'n¬g([l])', r'ng¬\1', code)
        if system == 'LIRA':
            code = re.sub(r'<<au¬t([lr])', r'aut¬\1', code)
            code = re.sub(r'<<uns¬([ptk])', r'un¬s\1', code)
            code = re.sub(r'¬(' + con + '+ed)>>', r'\1', code)
            code = re.sub(r'¬(' + con + '+es)>>', r'\1', code)
            code = re.sub(r'i¬ed>>', r'ied>>', code)
            code = re.sub(r'i¬es>>', r'ies>>', code)
        if system == 'PEND':
            code = re.sub(r'¬(' + con + '+ed)>>', r'\1', code)
            code = re.sub(r'¬(' + con + '+es)>>', r'\1', code)
            code = re.sub(r'¬(' + con + '+e)>>', r'\1', code)
            code = re.sub(r'([ao])¬w(e)', r'\1w¬\2', code)
            code = re.sub(r'([ao])¬y(i)', r'\1y¬\2', code)
            code = re.sub(r'<<uns¬?([ptck])¬?', r'un¬s\1', code)
            code = re.sub(r'(e)¬(a¬?r)', r'\1\2', code)
            code = re.sub(r'(n)([ptc])¬([lr])', r'\1¬\2\3', code)
            for c in ['oa']:
                code = re.sub(c[0] + '¬' + c[1], c, code)
            code = re.sub(r'<<¬?(de|re|pre)([ptc])¬?([lr])', r'\1¬\2\3', code)
            code = re.sub(r'<<¬?(de|re|pre)([s])¬?([ptc])', r'\1¬\2\3', code)
            code = re.sub(r'<<¬?('+con+'+)e¬a('+con+'+)(|s|es|ing|ed)>>', r'\1ea\2\3', code)
            for c in ['ee', 'au', 'aw', 'oo', 'eu', 'ew', 'oi', 'oy']:
                code = re.sub(c[0] + '¬' + c[1], c, code)
            code = re.sub(r'oing>>', r'o¬ing>>', code)
        if system in ('LIRA', 'PEND'):
            code = re.sub(r'¬(' + con + ')less>>', r'\1¬less>>', code)
            code = re.sub(r'¬(' + con + ')ness>>', r'\1¬ness>>', code)
        code = re.sub(r'¬(' + con + ')li>>', r'\1¬li', code)
        code = re.sub(r'¬(' + con + '+¬>>)', r'\1', code)
        code = re.sub(r'¬?<<(.)>>¬?', r'\1', code)
        #print('Watch:', code[-30:])
        code = re.sub(r'¬>>', r'>>', code)
        code = re.sub(r'¬ed>>', r'ed>>', code)
        code = re.sub(r'¬es>>', r'es>>', code)
        code = re.sub(r'<<¬+', r'<<', code)
        code = re.sub(r'¬(' + vow + dia + '?)>>', r'\1>>', code)
        code = re.sub(r'<<(' + trucon + '+' + dia + '?|' + vow + dia + '?)¬', r'<<\1', code)
        code = re.sub(r'(<<|>>)', r'', code)
        code = re.sub(r'¬', r'­', code)
    elif hyphenate and system == 'GOTH':
        vow = '𐌰𐌴𐌹𐌿𐍁𐍉'
        dia = '̈̔'
        con = '𐌱𐌲𐌳𐌶𐌷𐌸𐌺𐌻𐌼𐌽𐌾𐍀𐍂𐍃𐍄𐍆𐍇𐍈'
        trucon = con
        let = vow + dia + con
        vow, dia, con, let, trucon = [f'[{x}]' for x in [vow, dia, con, let, trucon]]
        code = re.sub(r'(' + let + '+)', r'<<\1>>', code)
        code = re.sub(r'(' + con + vow + ')', r'¬\1', code)
        code = re.sub(r'(' + vow + '|' + dia + ')(' + vow + ')', r'\1¬\2', code)
        code = re.sub(r'(𐌰|𐌴|𐍉)¬(𐌹|𐌿)', r'\1\2', code)
        #for c in ['ch', 'sh', 'th']:
        #    code = re.sub(c[0] + '¬' + c[1], '¬' + c, code)
        for c in ['𐌴𐌹', '𐌰𐌹', '𐌰𐌿', '𐌴𐌾', '𐍉𐌹', '𐍉𐌿', '𐌿𐌿', '𐍁𐌹', '𐍁𐌿']:
            code = re.sub(c[0] + '¬' + c[1], c, code)
        code = re.sub(r'¬([𐌻𐌼𐌽𐍂])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'¬(' + con + r')\1', r'\1¬\1', code)
        code = re.sub(r'¬([𐌻𐌼𐌽𐍂])(' + trucon + ')', r'\1¬\2', code)
        code = re.sub(r'([𐌱𐌲𐌳𐌺𐍀𐍆])¬([𐌻])', r'¬\1\2', code)
        code = re.sub(r'([𐌱𐌲𐌳𐌺𐍀𐍆])¬([𐍂])', r'¬\1\2', code)
        code = re.sub(r'(𐍇𐌹|𐍃𐌹)¬('+vow+')', r'\1\2', code)
        code = re.sub(r'([𐌱𐍀𐍂])𐍃¬([𐍀𐍄𐌺])', r'\1¬𐍃\2', code)
        code = re.sub(r'¬(' + con + ')𐌻𐌹>>', r'\1¬𐌻𐌹', code)
        code = re.sub(r'¬(' + con + '+¬>>)', r'\1', code)
        code = re.sub(r'¬>>', r'>>', code)
        code = re.sub(r'<<¬+', r'<<', code)
        code = re.sub(r'¬(' + vow + dia + '?)>>', r'\1>>', code)
        code = re.sub(r'<<(' + trucon + '+' + dia + '?|' + vow + dia + '?)¬', r'<<\1', code)
        code = re.sub(r'(<<|>>)', r'', code)
        code = re.sub(r'¬', r'­', code)
    else:
        code = re.sub('¬', '', code)
    return code


def postransliterate(code, posttranssytem):
    new_code = code
    if posttranssytem == 'CISALAT':
        transtable = {'А': 'A', 'А̂': 'Â', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Е̂': 'Ê', 'Ә': 'Ə',
                      'Ә̂': 'Ə̂', 'Ж': 'J', 'З': 'Z', 'Ӡ': 'Đ', 'И': 'I', 'И̂': 'Î', 'Ј': 'Y', 'К': 'K', 'Л': 'L',
                      'М': 'M', 'Н': 'N', 'О': 'O', 'О̂': 'Ô', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'Ꚋ': 'Ŧ',
                      'У': 'U', 'У̂': 'Û', 'Ү': 'W', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ç', 'Ш': 'Ş', 'Ь': 'Y',
                      'а': 'a', 'а̂': 'â', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'е̂': 'ê', 'ә': 'ə',
                      'ә̂': 'ə̂', 'ж': 'j', 'з': 'z', 'ӡ': 'đ', 'и': 'i', 'и̂': 'î', 'ј': 'y', 'к': 'k', 'л': 'l',
                      'м': 'm', 'н': 'n', 'о': 'o', 'о̂': 'ô', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ꚋ': 'ŧ',
                      'у': 'u', 'у̂': 'û', 'ү': 'w', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ç', 'ш': 'ş', 'ь': 'y'}
        for t in transtable:
            new_code = re.sub(t, transtable[t], new_code)
    return new_code


def convert_code(code, file_path=os.path.join(project_path, 'default.txt'), posttrans=None):
    # print(file_path)
    code = re.sub(r'\{[^}]+\}\{=([^}]+)\}', r'<=/\1/=>', code)  # {U.S.}{=Ю.С.}
    code = re.sub(r'&amp;', r'&#38;', code)
    code = re.sub(r'&quot;', r'&#34;', code)
    code = re.sub(r'&lt;', r'&#60;', code)
    code = re.sub(r'\{\{([^}]+)\}\}', r'<=/\1/=>', code)  # {{in vitro}}
    code = re.sub(r'\{(\d)\}', r'\1', code)  # use{1}
    code = re.split('(<[^>]+>)', code)
    word_list = list()
    for n, text in enumerate(code):
        if n % 2 == 0:
            local_list = re.findall('[' + English_alphabet + '’]*[' + English_alphabet + '][0-9]?', text.lower())
            word_list += local_list
    word_list = sorted(list(set(word_list)))
    word_list_path = re.sub(r'\.[a-z]+\Z', '.WordList.txt', file_path)
    with open(word_list_path, 'wt', encoding='utf8') as word_list_file:
        word_list_file.write('\n'.join(word_list))
    cyr_dict = make_local_dictionary(file_path, word_list)
    for n, text in enumerate(code):
        if n % 2 == 0:
            code[n] = convert_text(text, cyr_dict)
            if posttrans:
                code[n] = postransliterate(code[n], posttrans)
    code = ''.join(code)
    if system == 'CIRA':
        code = re.sub(r'-([вдслмр]|нт)\b', chr(0x2011)+r'\1', code)
    code = re.sub(r'<=/([^}]+?)/=>', r'\1', code)  # {{in vitro}}
    code = re.sub(r'­’', r'’', code)  # soft hyphens before apostrophes
    if not hyphenate:
        code = re.sub(r'­', r'', code)
    return code


def convert_file(file_path, posttrans=None, odt=False): # odt: open document text
    print('convert_file', file_path)
    with open(file_path, mode='rt', encoding='utf8') as f:
        code = f.read()
    if odt:
        code = re.sub('<office:binary-data>', '<office:binary-data><', code)
        code = re.sub('</office:binary-data>', '></office:binary-data>', code)
        code = re.sub('&quot;', '&#34;', code)
        code = re.sub('&amp;', '&#38;', code)
        code = re.sub('&apos;', '&#39;', code)
        code = re.sub('&lt;', '&#60;', code)
        code = re.sub('&gt;', '&#62;', code)
        split_code = re.split(r'(</?office:body>|</?body>)', code)
        split_code[2] = convert_code(split_code[2], posttrans=posttrans)
        code = ''.join(split_code)
        code = re.sub('<office:binary-data><', '<office:binary-data>', code)
        code = re.sub('></office:binary-data>', '</office:binary-data>', code)
    else:
        code = convert_code(code, posttrans=posttrans)
    output_path = re.sub(r'(.*)\.([a-zA-Z0-9]+)', r'\1.'+system+r'.\2', file_path)
    with open(output_path, mode='wt', encoding='utf8') as f:
        f.write(code)
    print('Input file:\n', file_path)
    print('Output file:\n', output_path)


def main():
    file_path = os.path.join(
        project_path, 'Examples',
        'Eoin Colfer. Artemis Fowl 01.html'
    )

    file_path = r'/home/hellerick/Dropbox/Lib/Fiction/Stewart, Mary/Stewart, Mary - The Little Broomstick.code.txt'

    print(file_path)
    # convert_file(file_path, posttrans='CISALAT')
    if 0:
        convert_file(file_path, odt=True)

    else:
        print(convert_code('''
The letter Wyn is too similar to the letter P so I don’t like the idea.
'''))

    try:
        print(watch)
    except NameError:
        pass


##    print(hyphenate_code("'petróleum'"))


if __name__ == '__main__':
    main()
