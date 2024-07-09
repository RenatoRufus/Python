nome = 'Luiz otávio'
altura = 1.73
peso = 150
imc = peso / altura ** 2

#f-string" 
linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'{peso} quilos e seu imc é,'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

