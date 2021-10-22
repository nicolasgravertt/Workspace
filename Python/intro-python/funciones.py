def miFuncion():
    print('Mi primera funcion')

def imprimeDato(argumentouno):
    print('Mi argumento es',argumentouno)

#imprimeDato('parametro 1')

def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

#si llamo de esta forma un metodo no importa el orden en el que se ingresen sus argumentos siempre y cuando el nombre especifico se declare junto a un igual.
#nombreCompleto(nombre='Chanchito',apellido='Feliz')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

nombreCompleto2(nombre='Chanchito',apellido='Feliz')

#si llamo mifuncion2() sin argumento este tomara el valor asignado de 'Chanchito' pero si le asigno un valor a mifuncion2('Batman') este imprimira Batman
def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

#miFuncion2()
#miFuncion2('Batman')

def miFuncionLista(lista):
    for el in lista:
        print(el)

miFuncionLista(['Chanchito','Feliz'])