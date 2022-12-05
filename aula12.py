nome = 'Diego'
altura = 1.80
peso = 72
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu IMC é,'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
# O (F) na frente de str são chamados de f-strings ou seja: Formatação de strings
