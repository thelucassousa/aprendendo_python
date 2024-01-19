'''
Recebemos uma variável com o nome de uma professora da escola para inserimos no cadastro. No entanto, precisamos tratar esse texto antes de inserirmos no sistema.
'''
texto = '   Geovana Alessandra dias Sanyos   '

'''
O objeto final é que o nome esteja da seguinte forma:
-> GEOVANA ALESSANDRA DIAS SANTOS
'''
#método converte tudo para minúscula:
texto = str.lower(texto)


#método que converte tudo para maiúscula:
texto = str.upper(texto)

#método remove os espaços do início e do fim de uma string:
texto = str.strip(texto)

#método para substituir todas as ocorrências do texto "antigo" na string por "novo"
texto = texto.replace('Y', 'T')

print(texto)