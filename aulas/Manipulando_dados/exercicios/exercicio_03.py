#3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.  

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Quantos metros você tem? '))
print(f'Olá {nome}, você tem {idade} anos e sua altura é {altura} m.')