import os, time
from datetime import datetime
ant = 0
while 1:
  tam = os.stat(arq).st_size
  agora = datetime.now() # .__format__("%y/%m/%d - %H:%M")
  print "{}: {} - {}G dif: {}M".format(agora, tam, tam/1024/1024/1024, (tam-ant)/1024/1024)
  ant = tam
  time.sleep (30)

