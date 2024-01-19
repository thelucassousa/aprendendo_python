'''
Escreva um programa em Python que solicite ao usuário o seu nome, o ano de ingresso na escola e a nota do teste de ingresso. Em seguida, exiba uma mensagem de boas-vindas personalizada, informando o nome do estudante, o ano de ingresso e a nota do teste de ingresso.
'''

nome_aluno = input('Olá, qual seu nome? ')
ano_ingresso = int(input('Qual foi seu ano de ingresso? '))
nota_corte = float(input('E qual foi sua nota corte? '))

if ano_ingresso == 2024: 
    print(f'Olá {nome_aluno}, então você está presente na escola desde 2024, seja muito bem vindo, sua nota de corte foi {nota_corte}')
else:
    print(f'Olá {nome_aluno}, então você está presente na escola desde {ano_ingresso}, é um prazer ter você aqui! Sua nota de corte foi {nota_corte}')

