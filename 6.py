import argparse
from random import sample

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('inp1', type=str)
    with open(parser.parse_args().inp1, 'r', encoding='utf8') as f:
        s = [str(el).strip() for el in f.readlines()]
        print(s)
        x = True
        for key, el in enumerate(s):
            if key == 0 and str(el).startswith('def'):
                x = False
            else:
                if str(el).startswith('def'):
                    if str(s[key - 1]).startswith('#'):
                        pass
                    else:
                        x = False
        print(x)

except:
    print('Ошибка')
