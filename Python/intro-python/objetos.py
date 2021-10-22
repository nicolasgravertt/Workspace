#class Usuario:
#    nombre = "Felipe"
#    apellido = "Feliz"
#
#usuario = Usuario()
#
#print(usuario.nombre,usuario.apellido)

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es ' , self.nombre,self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, mi nombre es ', self.nombre,self.apellido, ' y soy administrador')

#usuario = Usuario('Felipe','Feliz')
#usuario2 = Usuario('Chanchito','Feliz')
#
#print(usuario.nombre,usuario.apellido,usuario2.nombre,usuario2.apellido)
#
#usuario.saludo()
#usuario.nombre = 'Nicolas'
#usuario.saludo()
#
#admin = Admin('Super','Feliz')
#admin.saludo()
#admin.superSaludo()

#eliminar el atributo nombre del usuario
#del usuario.nombre
#Eliminar la instancia usuario
#del usuario

class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola soy un ',self.tipo,' y mi sonido es el: ',self.onomatopeya)

class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self,nombre, onomatopeya)
        print('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'Perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

gato = Gato('fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais','ladrido')
perro.saludo()