from datetime import timedelta, datetime

def iatar(h, m):
  return datar(str(h) + ':' + str(m))

def datar(str):
  return datetime.strptime(str, '%H:%M')

prent = datar('07:50')
prsai = datar('11:55')
seent = datar('12:55')
josta = seent + ( timedelta(minutes=480) - (prsai - prent) - timedelta(minutes=35) )
print iatar(17, 45) + timedelta(minutes=35)
#esexent = exsai - timedelta(minutes=120)
