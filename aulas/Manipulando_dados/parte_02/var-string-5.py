'''Escreva um programa em Python que pede ao usuário para digitar uma frase e, em seguida, imprime a mesma frase com todas as palavras em maiúsculo, sem espaços em branco no início e no final de cada palavra e substitua o "a" pelo "u".'''


frase_usuario = input("Escreva uma frase: ");
print(frase_usuario.strip().replace("a", "u").upper())

