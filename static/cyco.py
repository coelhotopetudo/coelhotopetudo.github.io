import os
filler = {}

def carregar():
  comandos = open('chomandos.txt')
  filler = {}
  for comando in comandos:
    dados = comando.split(';')
    filler[dados[0]] = dados[1]
  return filler

def quest(cmdLs, res):
  return str(raw_input(res + ' - ZZ sai: '))

def getch(cmdLs, res):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

filler = carregar()
cmdLs = filler.get('aa')

dig = getch(cmdLs, 'i')

while (dig != 'Z'):
  filler = carregar()
  if (dig == '.'):
    dig = res
  if (dig in filler):
    cmd = filler.get(dig)
    os.system(cmd)
    res = dig
  else:
    res = 'ERRO: ' + dig
  dig = getch(cmdLs, res)
print 'saiu'
