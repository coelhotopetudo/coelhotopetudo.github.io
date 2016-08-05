# coding: iso8859-1
linhas = ''',Rendimentos tributáveis,zrra_VL_RENDIME_JAN
$F{RENDIMENTOS_ISENTOS}.contains(ECamposRendimentos.ISENCAO_PENSAO_MOLESTIA.getKey()),Rendimento isento moléstia grave,zrra_VL_MOLESTIA_JAN
$F{DEDUCAO}.contains(ECamposRendimentos.DEDUCAO_PREVIDENCIA_OFICIAL.getKey()),Previdência oficial,zrra_VL_DEDUCAO_PO_JAN
$F{DEDUCAO}.contains(ECamposRendimentos.DEDUCAO_PENSAO_ALIMENTICIA.getKey()),Pensão alimentícia,zrra_VL_DEDUCAO_PA_JAN
,Imposto Retido,zrra_VL_RETIDO_JAN
,Parcela isenta aposentadoria 65 anos,zrra_VL_RIP65_JAN
,Despesas com ação judicial,zrra_VL_CUSTAS_JAN'''

res = ''
res += '<subreport>'
res += '<reportElement positionType="Float" x="0" y="60" width="555" height="5" isRemoveLineWhenBlank="true"/>'
res += '<subreportParameter name="TITULO"><subreportParameterExpression><![CDATA["Totais"]]></subreportParameterExpression></subreportParameter>'
for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split(' '):                                
  total = ''
  for linha in linhas.split('\n'):
    dados = linha.split(',')
    prefixo = dados[2]
    prefixado = prefixo[0:len(prefixo)-3] + mes
    total += '$F{' + prefixado + '}+'
  # suprimindo o ultimo +
  total = total[0:len(total)-1]
  res += '<subreportParameter name="%(mes)s"><subreportParameterExpression><![CDATA[%(total)s]]></subreportParameterExpression></subreportParameter>' % vars()
res += '<subreportExpression><![CDATA[$P{SUBREPORT_DIR} + "Mensais_Valores.jasper"]]></subreportExpression></subreport>'
print res
