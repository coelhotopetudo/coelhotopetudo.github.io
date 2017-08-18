# -*- coding: utf-8 -*-

from unicodedata import normalize

def remover_acentos(txt, codif='utf-8'):
  return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

print remover_acentos('[ACENTUAÇÃO] ç: áàãâä! éèêë? íì&#297;îï, óòõôö; úù&#361;ûü.').replace(' ', '').lower()
