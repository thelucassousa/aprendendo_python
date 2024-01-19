'''
Suponha que você está trabalhando em uma loja de eletrônicos e precisa calcular o preço final de um produto para o cliente.
O preço base do produto é de R$ 1500,00, porém, é necessário adicionar o valor do imposto de 15% sobre o preço base e também o valor do frete, que é de R$ 50,00.
Crie um programa que armazene o preço base do produto, o valor do imposto e o valor do frete em variáveis. Em seguida, calcule e exiba o preço final do produto para o cliente.
Lembre-se de realizar os cálculos corretamente e exibir o resultado de forma organizada
'''

print('Olá, seja bem vindo!')
valor_produto = float(input('Qual valor inicial do produto? '))

frete = 50
preco_final = valor_produto + (valor_produto * 0.15) + frete

print(f'O valor final é R$ {preco_final}')