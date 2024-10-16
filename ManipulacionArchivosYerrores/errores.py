#print(0/0)
#print(result)
print('Hola')

suma = lambda x,y: x + y
#suma = lambda x,y: x + (y * 2)
assert suma(2,2)== 4

print('Hola 2')

age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')

print('Hola 3')
