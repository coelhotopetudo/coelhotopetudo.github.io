ori = ''
with open('firebird.sql', 'r') as arq:
  for linha in arq:
    ori = ori + linha 
sql = ori
import fdb
db='/var/lib/firebird/DIRF2017001403030001002016.FDB'
cur = fdb.connect(dsn=db,user='sysdba',password='masterkey').cursor().execute(sql)

nomes=''
for fieldDesc in cur.description:
  nomes=nomes + fieldDesc[fdb.DESCRIPTION_NAME] + ', '
print nomes

print cur.fetchall()

