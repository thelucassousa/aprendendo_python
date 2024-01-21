# 12. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

print('Média de notas')
nota_01 = float(input('Qual a primeira nota do estudante? '))
nota_02 = float(input('Qual a segunda nota do estudante? '))
nota_03 = float(input('Qual a terceira nota do estudante? '))

media = (nota_01 + nota_02 + nota_03) / 3

print(f'A média do aluno é: {media}')