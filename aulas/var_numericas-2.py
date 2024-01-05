'''
1 - Crie um programa que armazene as informações de salário e quantidade de funcionários de três departamentos de uma empresa.
Em seguida, calcule e exiba a média salarial de cada departamento e a média salarial geral da empresa.

Lembre-se de declarar as variáveis necessárias, realizar os cálculos e exibir os resultados de forma organizada.'''

#Salário dos departamentos:
sal_depto_1 = 5000 
sal_depto_2 = 7200 
sal_depto_3 = 8600 

mult_sal = sal_depto_1 + sal_depto_2 + sal_depto_3

#Quantidade de funcionárias por departamento:
qtde_func_dept_1 = 12
qtde_func_dept_2 = 8
qtde_func_dept_3 = 5

#quantidade total de funcionárias:
qtde_total_func = qtde_func_dept_1 + qtde_func_dept_2 + qtde_func_dept_3

#media salaria
media_dpto_1 = (sal_depto_1 * qtde_func_dept_1) / qtde_func_dept_1
media_dpto_2 = (sal_depto_2 * qtde_func_dept_2) / qtde_func_dept_2
media_dpto_3 = (sal_depto_3 * qtde_func_dept_3) / qtde_func_dept_3

#print media salarial de cada departamento
print(f"A media salarial do departamento 1 é {media_dpto_1} \r\nA media salarial do departamento 2 é {media_dpto_2} \r\nA media salarial do departamento 3 é {media_dpto_3} ")

#media salarial da empresa
media_empresa = (qtde_total_func + mult_sal) / mult_sal
print(f'A media salarial da empresa é: {media_empresa}')
