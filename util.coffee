fs = require 'fs'

bc = module.exports = () ->

bc.show = (msg) -> console.log(msg)

bc.codificar = (nome) ->
  ent = ->
    fs.readFileSync nome, 'utf8'
  numeros = ent().split('\n')
  res = ''
  # por causa da ultima linha do arquivo
  res += "#{bc.gerarCodificacao(numeros[j])}" for j in [0..(numeros.length-2)]
  sai = ->
    fs.writeFile '/home/00737990929/doc/out/tst/codificar.html', "#{bc.getIni('cod')}\n#{res}\n#{bc.getFim()}"
  sai()
  return res

bc.descodificar = (nome) ->
  ent = ->
    fs.readFileSync nome, 'utf8'
  numeros = ent().split('\n')
  res = ''
  # por causa da ultima linha do arquivo
  res += "#{bc.gerarDescodificacao(numeros[j])}" for j in [(numeros.length-2)..0]
  sai = ->
    fs.writeFile '/home/00737990929/doc/out/tst/descodificar.html', "#{bc.getIni('des')}\n#{res}\n#{bc.getFim()}"
  sai()
  return res

bc.array2yrra = (array) ->
  i = 0
  yrra = []
  yrra[i++] = array[j] for j in [(array.length-1)..0]
  return yrra

bc.getIni = (tp) ->
  ini = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="http://siscop.portalcorporativo.serpro/" />
<title>ponto</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">#{tp} ponto</td></tr>
</thead><tbody>"""
  return ini

bc.getFim = () ->
  fim = '''</tbody></table></body></html>'''
  return fim

bc.inverter = (nome) ->
  ent = ->
    fs.readFileSync nome, 'utf8'
  numeros = ent().split('\n')
  res = ''
  # por causa da ultima linha do arquivo
  res += "#{numeros[j]}, " for j in [(numeros.length-2)..1]
  res += numeros[0]
  return res

bc.gerarDescodificacao = (dia) ->
  res = " <tr> <td>clickAndWait</td> <td>link=#{dia}</td> <td></td> </tr>"
  res += '<tr> <td>type</td> <td>id=cboOcorrencia4</td> <td></td> </tr>'
  res += '<tr> <td>clickAndWait</td> <td>id=submit1</td> <td></td> </tr>\n'
  return res

bc.gerarCodificacao = (dia) ->
  res = " <tr> <td>clickAndWait</td> <td>link=#{dia}</td> <td></td> </tr>"
  res += '<tr> <td>sendKeys</td> <td>id=cboOcorrencia4</td> <td>25</td> </tr>'
  res += '<tr> <td>select</td> <td>id=CBOcboOcorrencia4</td> <td>label=25-Flexibilidade</td> </tr>'
  res += '<tr> <td>clickAndWait</td> <td>id=submit1</td> <td></td> </tr>\n'
  return res
