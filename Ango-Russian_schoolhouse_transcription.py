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


def convert_text(text):
    pass

def convert_file(file_path):
    with open(file_path, mode='rt', encoding='utf8') as f:
        code = f.read()
    code = re.split('(<[^>]+>)', code)
    print(code[:50])
    word_list = list()
    for n, text in enumerate(code):
        if n%2 == 0:
            local_list = re.findall('[+English_alphabet+’]*['+English_alphabet+']', text)
            word_list += local_list
    word_list = sorted(list(set(word_list)))
    word_list_path = re.sub(r'\.[a-z]+\Z', 'WordList.txt', file_path)
    with open(word_list_path, 'wt', encoding='utf8') as word_list_file:
        word_list_file.write('\n'.join(word_list))
    for n, text in enumerate(code):
        if n%2 == 0:
            code[n] = convert_text(text)
    print(code[:50])


def main():

    file_path = os.path.join(
        project_path, 'Examples',
        'Eoin Colfer. Artemis Fowl 01.html'
    )

    convert_file(file_path)


if __name__ == '__main__':
    main()