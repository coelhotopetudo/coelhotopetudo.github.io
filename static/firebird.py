def out(str, arq):
  print str
#  arq.write(str)

ori = ''

res = open('/tmp/res.txt', 'w')
with open('firebird.sql', 'r') as arq:
  for linha in arq:
    ori = ori + linha 
sql = ori
import fdb
db='/var/lib/firebird/dirfteste.FDB'
#db='/home/00737990929/workspace/dirf/01/29-DIRF_JAVA/db/DIRF2017415636710001482016.FDB'
cur = fdb.connect(dsn=db,user='sysdba',password='masterkey').cursor().execute(sql)

nomes=''
for fieldDesc in cur.description:
  nomes=nomes + fieldDesc[fdb.DESCRIPTION_NAME] + ', '

out(nomes, res)
out(str(cur.fetchall()), res)

