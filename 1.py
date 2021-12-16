import argparse

parser = argparse.ArgumentParser()
parser.add_argument('indir', type=str)

arg = parser.parse_args().indir
try:
    with open(arg, 'r', encoding='utf8') as r:
        print(r.read(10))
except:
    print('Error')
