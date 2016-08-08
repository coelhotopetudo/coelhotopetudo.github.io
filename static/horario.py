from datetime import timedelta, datetime

def datar(str):
  return datetime.strptime(str, '%H:%M')

prent = datar('07:56')
prsai = datar('11:33')
esprsai = prent + timedelta(minutes=299)
seent = datar('13:55')
sesai = datar('17:00')
exent = datar('17:00')
exsai = datar('18:45')
esexent = exsai - timedelta(minutes=120)
essesai = seent + timedelta(minutes=239)
essesai = esexent
esseent = essesai - timedelta(minutes=180)
esexsai = exent
print prent
print 'prsai: %s - %s' % (prsai, esprsai)
print 'seent: ' + str(seent) + ' - ' + str(esseent)
print 'sesai: %s - %s' % (sesai, essesai)
print 'exent: %s - %s' % (exent, esexent)
print 'exsai: %s - %s' % (exsai, esexsai)
