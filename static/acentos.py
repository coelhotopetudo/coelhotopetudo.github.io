# -*- coding: utf-8 -*-

from unicodedata import normalize
import csv

def remover_acentos(txt, codif='utf-8'):
  return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore').replace(' ', '').lower()

with open('/home/alisson/Downloads/presentation_type.csv') as f:
  spamreader = csv.reader(f, delimiter=',', quotechar='"')
  for line in spamreader:
    cont = '# ' + line[3] + ': ' + line[2]
    cont += '\n\n'
    cont += line[6]
    cont += '\n\n'
    cont += 'curriculo: ' + line[5]
    cont += '\n\n'
    desa = remover_acentos(line[1])
    open('/tmp/' + desa + '.md', 'a').write(cont)

res = 'fim'
print res
