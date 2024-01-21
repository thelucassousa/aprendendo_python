# 9. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

print('Olá, vamos trabalhar com potência')
valor_01 = int(input('Qual o valor que você deseja a exponenciação? '))
valor_exponeciado = int(input('Digite o valor de exponiação (lembrando que deve ser um número inteiro)'))

exponenciacao = valor_01 ** valor_exponeciado

print(f'O {valor_01} exponenciado por {valor_exponeciado} é {exponenciacao}')