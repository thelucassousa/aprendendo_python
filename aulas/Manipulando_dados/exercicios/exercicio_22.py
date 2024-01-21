# 22. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.  

print('Trocando "a" por "@"')
frase = str.lower(input('Escreva uma frase: '))
print(f'você escreveu:\r\n"{frase.replace("a", "@")}"')