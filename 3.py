import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('inp1', type=str)
    with open(parser.parse_args().inp1, 'r', encoding='utf8') as f:
        with open('file_new', 'w', encoding='utf8') as f1:
            s = f.readlines()
            for key, el in enumerate(s):
                f1.write(f'{key + 1}: {el}')
except:
    print('Ошибка')
