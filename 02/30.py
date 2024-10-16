

print(123)
print(456)
#int('a')

numero_str = input('Vou dobrar o numero: ')

try:

    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('Isso não é um número')


