# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
print('a' + 'b')  #polimorfismo
#print('1' + 1)  erro
print(int('1') + 1)


print('1', type('1'))
print(int('1'), type('1'))
print(type(float('1') + 1))

print(bool('')) #false
print(bool(' ')) #true  -  espaço
print(str(11) + 'b')
