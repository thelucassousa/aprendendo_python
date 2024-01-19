'''
Existem funções para conversão de valores
- Inteiros: int(dados_para_conversão);
- Float: float(dados_para_conversão);
- String: str(dados_para_conversão);
- Booleano: bool(dados_para_conversão);;
 
Exemplo, o ingresso de um estudando na escola:
'''

ano_entrada = int(input('Escreva o ano de ingresso do(a) estudante: '))
print(type(ano_entrada), ano_entrada)

nota_entrada = float(input('Escreva a nota de entrada: '))
print(type(nota_entrada), nota_entrada) 

print(f'O ano de entrada é {ano_entrada} com nota de corte de {nota_entrada}')