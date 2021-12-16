import argparse
from random import sample

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('inp1', type=str)
    with open(parser.parse_args().inp1, 'r', encoding='utf8') as f: # В файле хранится тескт вида ['dwdw', 'fefe']
        s = [str(el).capitalize() for el in f.read().strip('[]').split(', ')]
        print(''.join(sample(s, 2)))

except:
    print('Ошибка')
