# 10. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0. 

print('Divisão inteira')
valor_01 = int(input('Digite o valor que você quer dividir: '))
divisor = int(input('Digite por quanto você quer dividir (Lembrando que não pode ser 0 e deve ser inteiro)'))

divisao = valor_01 // divisor

print(f'o {valor_01} dividido por {divisor} é {divisao}')