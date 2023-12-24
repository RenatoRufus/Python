#operadores lógicos
#none - sem valor
# python false - 0 0.0 ''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')    

#avaliação de curto circuito
print(True and True and True)

print(bool(''))  #false
print(bool(0.0)) #false
print(bool(0)) #false

if 0 and 1:
    print(True and 1)

