# 21. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.


print('Trocando "e" por "f"')
frase = str.lower(input('Escreva uma frase: '))
print(f'você escreveu:\r\n"{frase.replace("e", "f")}"')