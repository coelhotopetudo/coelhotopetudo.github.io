---
layout: post
title: 'Gerador de subrelatório para o jasper usando python'
--- 

Gerador de parametros para jasper, antes eram fields.

REPARAR que para não causar conflito com o liquid, foi adicionada uma barra entre '$P{\%('

```
# coding: iso8859-1
def gerar(linhas):
        res = ''
        ycont = 10
        tamanho = 5

        # TEMP
        res += '<jasper>'

        for linha in linhas.split('\n'):
          dados = linha.split(',')
          condicao = dados[0]
          rotulo = dados[1]
          prefixo = dados[2]

          res += '<subreport>'
          res += '<reportElement positionType="Float" x="0" y="%(ycont)s" width="555" height="5" isRemoveLineWhenBlank="true"/>' % vars()

          if (condicao != ''):
            res = res[0:len(res)-2] + '><printWhenExpression><![CDATA[%(condicao)s]]></printWhenExpression></reportElement>' % vars()

          res += '<subreportParameter name="TITULO"><subreportParameterExpression><![CDATA["%(rotulo)s"]]></subreportParameterExpression></subreportParameter>' % vars()

          for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split(' '):                                
            # os dados de entrada terminam com 'JAN'
            prefixado = prefixo[0:len(prefixo)-3] + mes
            res += '<subreportParameter name="%(mes)s"><subreportParameterExpression><![CDATA[$P{\%(prefixado)s}]]></subreportParameterExpression></subreportParameter>' % vars()

          res += '<subreportExpression><![CDATA[$P{SUBREPORT_DIR} + "Mensais_Valores.jasper"]]></subreportExpression></subreport>'
          ycont += tamanho

        res += '</jasper>'

        return res

linhas = ''',Rendimentos tributáveis,zrra_VL_RENDIME_JAN
$F{RENDIMENTOS_ISENTOS}.contains(ECamposRendimentos.ISENCAO_PENSAO_MOLESTIA.getKey()),Rendimento isento moléstia grave,zrra_VL_MOLESTIA_JAN
$F{DEDUCAO}.contains(ECamposRendimentos.DEDUCAO_PREVIDENCIA_OFICIAL.getKey()),Previdência oficial,zrra_VL_DEDUCAO_PO_JAN
$F{DEDUCAO}.contains(ECamposRendimentos.DEDUCAO_PENSAO_ALIMENTICIA.getKey()),Pensão alimentícia,zrra_VL_DEDUCAO_PA_JAN
,Imposto Retido,zrra_VL_RETIDO_JAN
,Parcela isenta aposentadoria 65 anos,zrra_VL_RIP65_JAN
,Despesas com ação judicial,zrra_VL_CUSTAS_JAN'''
res = gerar(linhas)
arq = 'jr.xml'
open(arq, 'w').write(res)
```
