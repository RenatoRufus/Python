nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

print(" \n")

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

print("\n")

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato)