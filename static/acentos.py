# -*- coding: utf-8 -*-

from unicodedata import normalize
import csv

def remover_acentos(txt, codif='utf-8'):
  return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore').replace(' ', '').lower()

with open('/home/alisson/Downloads/presentation_type.csv') as f:
  spamreader = csv.reader(f, delimiter=',', quotechar='"')
  for line in spamreader:
    desa = remover_acentos(line[1])
    cabe = '-------------------------------\n'
    cabe += 'title: ' + line[1] + '\n'
    cabe += 'image: ' + desa + '\n'
    cabe += '------------------------------\n'
    cabe += '![' + line[1] + ']({{ site.baseurl }}/images/{{ page.image }}.jpg)\n'
    cabe += '\n\n'
    arq = open('/tmp/' + desa + '.md', 'w')
    arq.write(cabe)
    arq.close()

with open('/home/alisson/Downloads/presentation_type.csv') as f:
  spamreader = csv.reader(f, delimiter=',', quotechar='"')
  for line in spamreader:
    print line[2]
    cont = '# ' + line[3] + ': ' + line[2]
    cont += '\n\n'
    cont += line[6]
    cont += '\n\n'
    cont += '## Currículo\n'
    cont += line[5]
    cont += '\n\n'
    cont += '[Clique aqui para ver na grade](http://sistema.ftsl.org.br/ftsl9/grade/detail.html?pid=' + line[0] + ')'
    cont += '\n\n'
    desa = remover_acentos(line[1])
    open('/tmp/' + desa + '.md', 'a').write(cont)

res = 'fim'
print res
