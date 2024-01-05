'''
Temos 5 seguranças com salário de R$ 3k
Temos 16 docentes com salário de R$ 6k
Temos 1 Diretoria com salaário de R$ 12.5k

1 - Faça o levantamento de quantos funcionárias temos
2 - Faça a diferença do maior salário com o menor
3 - Faça a média ponderada dos salários
'''

qtde_segurancas = 5
qtde_docentes = 16
qtde_diretoria = 1

sal_seguranca = 3000
sal_docentes = 6000
sal_diretoria = 12500

qtde_total = qtde_diretoria + qtde_docentes + qtde_segurancas # total de empregados
dif = sal_seguranca - sal_diretoria #diferença dos salários 
media_ponderada = (qtde_segurancas * sal_seguranca + qtde_docentes * sal_docentes + qtde_diretoria + sal_diretoria) / qtde_total # a media

print(f"quantidade de funcionária: {qtde_total} '\r\n' a diferença salarial: {dif}'\r\n' a media ponderada dos salários: {media_ponderada}")