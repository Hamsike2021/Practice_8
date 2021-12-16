import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('inp1', type=str)
    parser.add_argument('inp2', type=str)


    def summ():
        with open(parser.parse_args().inp1, mode='r', encoding='utf8') as f:
            with open(parser.parse_args().inp2, mode='r', encoding='utf8') as f1:
                return f.read() + f1.read()
    print(summ())

except:
    print('Ошибка')
