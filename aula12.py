nome = 'Rufus'
altura = 2.4
peso = 95
imc = peso / altura ** 2


linha_1 = f'nome {nome} {altura:,.2f} {peso}'
linha_2 = f'IMC : {imc}'

print(linha_1)
print(linha_2)