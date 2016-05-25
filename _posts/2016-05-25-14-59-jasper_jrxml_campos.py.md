# :map <Enter> :w <Bar> !python % <CR>
import os

def montarOriginal(prefixo, arquivo):
  """formata o nome de arquivo necessario para criacao da copia do original

  >>> montarOriginal('pre', 'arq')
  'pre-arq'
  """
  return prefixo + '-' + arquivo

def copiarOriginal(prefixo, arquivo):
  """Faz a copia do arquivo original

  >>> import os
  >>> nome = 'DeclaracaoCompleta_BFC_Judicial.jrxml'
  >>> os.system('echo "cont1" > ' + nome)
  0
  >>> copiarOriginal('p', nome)
  '/hoje/campo/p-DeclaracaoCompleta_BFC_Judicial.jrxml'
  """
  original = montarOriginal(prefixo, arquivo)
  retorno = getDestino() + original
  os.system('cp ' + getOrigem() + arquivo + ' ' + getDestino() + arquivo)
  os.system('cp ' + getOrigem() + arquivo + ' ' + retorno)
  return retorno

def getDestino():
  return '/hoje/campo/'

def getOrigem():
  return '/home/00737990929/workspace/dirf/01/29-DIRF_JAVA/src/main/java/relatorios/'

def exc(prefixo, arquivo):
        copiarOriginal(prefixo, arquivo)
        caminho = getDestino()
        fields = open(caminho + prefixo + '-fields.txt', 'w')
        campos = open(caminho + prefixo + '-campos.txt', 'w')
        fed = caminho + prefixo + '.sed'
        zed = open(fed, 'w')
        with open(caminho + arquivo) as f:
          for line in f:
            if 'field' in line:
              alvo = line
              inicio = line.index('"') + 1
              parcial = line[inicio:len(line)]
              tamanho = parcial.index('"')
              campo = line[inicio:inicio+tamanho]
              prefixado = prefixo + '_' + campo
              select = prefixo + "." + campo + ' as ' + prefixado + ', '
              field = line[0:inicio] + prefixado + line[inicio+tamanho:len(line)]
              campos.write(select)
              fields.write(field)
              sed = 'sed -f "s/' + campo + '/' + prefixado + '/g" ' + caminho + arquivo + '\n'
              sed = 'cat ' + caminho + arquivo + ' | sed "s/' + campo + '/' + prefixado + '/g" > ' + caminho + arquivo + '\n'
              sed = 'sed -e "s/' + campo + '/' + prefixado + '/g" ' + caminho + arquivo + ' > ' + caminho + prefixo + arquivo + '\n'
              sed = 's/' + campo + '/' + prefixado + '/g\n'
              zed.write(sed)
              alvo = sed
              alvo = 'fim'
              # return alvo
        ced = 'sed -f ' + fed + ' ' + caminho + prefixo + '-' + arquivo
        comando = ced + ' > ' + caminho + arquivo
        print comando
#        os.system(comando)


if __name__ == "__main__":
  import doctest
  doctest.testmod()
  prefixo = 'bfcr'
  arquivo = 'DeclaracaoCompleta_BFC_RendTrib.jrxml'
  print montarOriginal(prefixo, arquivo)
#  print exc('bfcj', 'DeclaracaoCompleta_BFC_Judicial.jrxml')
  print exc('bfci', 'DeclaracaoCompleta_BFC_RendIsento.jrxml')
