from datetime import timedelta, datetime

def iatar(h, m):
  return datar(str(h) + ':' + str(m))

def datar(str):
  return datetime.strptime(str, '%H:%M')

prent = datar('08:25')
prsai = datar('13:33')
esprsai = prent + timedelta(minutes=180)
seent = datar('13:23')
sesai = datar('17:00')
exent = datar('17:00')
exsai = datar('18:45')
esexent = exsai - timedelta(minutes=120)
essesai = seent + timedelta(minutes=180)
essesai = esexent
esseent = essesai - timedelta(minutes=180)
esexsai = exent
print prent
print 'prsai: %s - %s' % (prsai, esprsai)
print 'seent: ' + str(seent) + ' - ' + str(esseent)
print 'sesai: %s - %s' % (sesai, essesai)
print 'exent: %s - %s' % (exent, esexent)
print 'exsai: %s - %s' % (exsai, esexsai)
print (iatar(12, 1) - iatar(8 , 18)) + (iatar(16,38) - iatar(13,16))
