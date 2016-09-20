select distinct(1)
from  BENEFICIARIO_DECLARANTE bde 
inner join CODIGO_RECEITA cr on cr.CDR_ID = bde.CDR_ID
where bde.pes_id = 2
and cr.COMPROVANTE_PJ = '119'
order by cr.cod_receita

