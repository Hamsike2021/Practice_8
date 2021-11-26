try:
  with open(input(), 'r', encoding='utf8') as r:
    print(r.read(10))
except FileNotFoundError:
  print('Error')
