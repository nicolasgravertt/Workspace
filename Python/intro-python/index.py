# If statement
#if 5 > 3:
#    print('5 es mayor a 3')

# Concatenacion
x = 5
y = 'chanchito feliz'
#print(x,y)
email = 'nicolasgravertt@hotmail.com'
#print (email)
a,b,c = 'lala','lele','lili'
#print(a,b,c)
valor1 = valor2 = valor3 = 'chanchito feliz'
#print(valor1,valor2,valor3)
inicio = 'hola '
final = 'mundo'
#print(inicio + final)

#Tipos de datos
palabra = 'hola mundo' #string
oracion = "hola mundo comilla doble" #string
entero = 20 # integer
conDecimales = 20.2 # float
numComplejo = 1j # numero complejo
#print(palabra,oracion,entero,conDecimales,numComplejo)

# Listas
lista = [1,2,3,3]
lista2 = lista.copy()
#agregar datos a la lista
lista.append(4)
#limpia los datos de la lista
#lista.clear()
#Indica la cantidad de veces que un dato esta dentro de una lista.
#lista.count(3)
#Cuenta los elementos dentro de la lista
#len(lista2)
#print(lista,lista2,'cantidad de veces que se repite el 3 en la lista: ' + str(lista2.count(3)),'cantidad de datos: ' + str(len(lista2)))


listaTexto = ['Hola','Mundo','Chanchito Feliz']
#print(listaTexto[0])
#print(listaTexto)
#listaTexto.pop() # este elimina el ultimo elemento de la lista
#listaTexto.remove('Hola') # Elimina un elemento por su valor
#listaTexto.reverse() # invierte el orden de la lista
#listaTexto.sort() # Ordenar lista
#print(listaTexto)

#tuplas
# se diferencian de las listas ya que estas una vez creadas no se pueden modificar

tupla = ('Hola','Mundo','Somos','Tupla')
#print(tupla,tupla.count('Hola'),tupla.index('Mundo'),tupla[3])

#si queremos modificarla('Agregar,eliminar') debemos transformarla en una lista de la siguiente manera

listaTupla = list(tupla)
#print(listaTupla)

#Range
rango = range(6)
#print(rango)


#Diccionarios 
diccionario = {
    "nombre": "Chanchito Feliz",
    "raza": "Persa",
    "edad": 5
}
#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario['raza'])
#print(diccionario.get('nombre'))
diccionario['nombre']  = 'Cleopatra'
#print(diccionario)
#print(len(diccionario))
diccionario['ronronea'] = 'Si'
#print(diccionario)
#diccionario.pop('ronronea')
#print(diccionario)
#eliminar el ultimo valor que se agrego
#diccionario.popitem()
#print(diccionario)
copiaGato = diccionario.copy()
#otra forma de copiar un diccionario a otro
#copiaGato = dict(diccionario)
del(diccionario['ronronea'])
#Eliminar datos del diccionario
diccionario.clear()
#print(diccionario,copiaGato)

Floffy = {
    "nombre": "Floffy",
    "edad": 4
}

Mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Floffy": Floffy,
    "Mamba": Mamba
}

#print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad = 6)
#print(perritos)

#Booleanos
verdadero = True
falso = False

print(verdadero,falso)
