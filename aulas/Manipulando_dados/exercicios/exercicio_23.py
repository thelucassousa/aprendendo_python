# 23. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”. 

print('Trocando "s" por "$"')
frase = str.lower(input('Escreva uma frase: '))
print(f'você escreveu:\r\n"{frase.replace("s", "$")}"')