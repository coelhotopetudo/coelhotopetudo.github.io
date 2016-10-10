from datetime import timedelta, datetime

def datar(str):
  return datetime.strptime(str, '%M:%S')

imagem = '''01;Punk Rock de Galpao;00:45
02;Guri do Passauna;02:59
03;Vento Sul;06:17
04;Passado Polones;08:46
05;Mal-arranjado;10:55
06;Talagaco no Peito;13:39
07;Pia de bosta;16:24
08;Coracao de Pinhao;19:07
09;O suicidio da polaquinha;21:55
10;A ultima mateada;27:19'''

todas = imagem.split('\n')
i = len(todas)
antiga = datar('31:05')
cmd = 'ffmpeg -ss %(ini)s -t %(dif)s -i cavalo.mp3 %(num)s-%(nome)s.mp3'
while (i > 0):
    dados = todas[i-1].split(';')
    num = dados[0]
#trocar espaco por underscore
    nome = dados[1].replace(' ', '_')
    atual = datar(dados[2])
    ini = (atual - datar('00:00')).seconds
    dif = (antiga - atual).seconds
    i-=1
    antiga = atual
    res = cmd % vars()
    print res
