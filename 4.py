import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('inp1', type=str)
    with open(parser.parse_args().inp1, 'r', encoding='utf8') as f:
        s = [str(el).strip() for el in f.readlines()]
        s1 = []
        for el in s:
            s1.extend(list(filter(lambda x: len(x) == len(max(el.split(), key=lambda y: len(y))), s)))
        print(', '.join(list(filter(lambda x: len(x) == len(max(s1, key=lambda y: len(y))), s1))))
except:
    print('Ошибка')
