# 8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

print('Vamos dividir \r\n')
numero_01 = int(input('Digite um valor inteiro: '))
numero_02 = int(input('Digite o denominador pelo qual você quer dividir (lembrando que não pode ser 0): '))

if numero_02 <= 0: 
    numero_02 = int(input('Digite o denominador pelo qual você quer dividir (lembrando que não pode ser 0): '))
else:
    print(f'A multiplicação dos dois valores é {numero_01 * numero_02}')