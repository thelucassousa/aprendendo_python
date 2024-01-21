# 19. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.  

print('Removendo espaços')
frase = input('Escreva uma frase: ')
print(f'você escreveu:\r\n"{str.strip(frase)}"')