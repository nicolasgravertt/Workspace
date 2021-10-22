#dato = input('Ingrese dato: ')
#lista = ['hola','mundo','chanchito', 'feliz','dragones']

#if lista.count(dato) > 0:
    #print('el dato existe: ',dato)
#else:
    #print('el dato no existe: ',dato)

primero = input('ingrese primer numero: ')
segundo = input('ingrese primer segundo: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

print(primero + segundo)

if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste un un valor que no es entero, intenta denuevo')
else:
    print(primero + segundo)
