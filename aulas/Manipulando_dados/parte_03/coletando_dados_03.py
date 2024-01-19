'''
Escreva um programa em Python que solicite ao usuário o seu nome e a sua idade. Em seguida, calcule e exiba o ano em que o usuário completará 100 anos.'''

nome = input('Olá, qual seu nome? ')
idade = int(input('E qual é a sua idade? '))
print(f'Seja muito bem vindo {nome}, hoje você tem {idade} anos e daqui {100 - idade}, você terá 100 anos. Isso deverá ocorrer por volta de {2024 + (100 - idade)}')