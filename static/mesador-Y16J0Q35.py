# coding: iso8859-1
TAM = 65
x = 0
modelo = '''
			<textField pattern="#,##0.0###">
				<reportElement positionType="Float" x="%(x)s" y="45" width="%(TAM)s" height="10" isRemoveLineWhenBlank="true"/>
				<textElement textAlignment="Right">
					<font fontName="Liberation Sans Narrow" size="8" isBold="false"/>
				</textElement>
				<textFieldExpression><![CDATA[$F{ZRRA_QTDE_MESES_%(mes)s}]]></textFieldExpression>
			</textField>
'''
res = ''
for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split(' '):
  res += modelo % vars()
  x += TAM
print res
