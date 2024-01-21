# 20. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas. 

print('Removendo espaços e deixando em minúsculo')
frase = input('Escreva uma frase: ')
print(f'você escreveu:\r\n"{str.strip(frase).lower()}"')