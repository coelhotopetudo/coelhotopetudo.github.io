def carregar(arq):
    li = set()
    with (open(arq, 'r')) as wcol:
        for col in wcol:
            li.add(str(col).lower())
    return li

colunas = carregar('wcol.txt')
campos = carregar('yfie.txt')
faltando = campos - colunas
for quebrado in faltando:
    campo = quebrado[0:len(quebrado)-1]
    if 'molestia' in campo:
        print "'0' " + campo + ','
    else:
        print campo[0:4] + '.' + campo[5:len(campo)] + ' ' + campo + ','
