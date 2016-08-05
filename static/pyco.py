import os
filler = {}

def carregar():
  comandos = open('comandos.txt')
  filler = {}
  for comando in comandos:
    dados = comando.split(';')
    filler[dados[0]] = dados[1]
  return filler

def quest(cmdLs, res):
  return str(raw_input(res + ' - ZZ sai: '))

filler = carregar()
cmdLs = filler.get('aa')

dig = quest(cmdLs, 'ini')

while (dig != 'ZZ'):
  filler = carregar()
  if (dig == '.'):
    dig = res
  if (dig in filler):
    cmd = filler.get(dig)
    os.system(cmd)
    res = dig
  else:
    res = 'ERRO: ' + dig
  dig = quest(cmdLs, res)
print 'saiu'
