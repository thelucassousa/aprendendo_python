'''
Escreva um programa em Python que pede ao usuário para digitar uma frase e, em seguida, imprime a mesma frase com todas as letras em maiúsculo e sem espaços em branco no início e no final.
'''
name = input("Qual seu nome? ")
print(name.strip().upper())  