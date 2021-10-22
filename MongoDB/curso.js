// Crear Documento
// Documentos -> Objetos de tipo JSON

user1 = {
    'username': 'user1',
    'age': 27,
    'email': 'nicolasGravertt@hotmail.com'
}
// Insertar Dato
db.users.insertOne(user1);


// Retorna los documentos Json en la colleccion
db.users.find();

// Insertar mas de un documento en una linea
db.users.insertMany([
	{
    'username': 'user3',
    'age': 247,
    'email': 'nicolasGravertt@hotmail.com'
	},
  {
    'username': 'user4',
    'age': 255,
    'email': 'nicolasGravertt@hotmail.com'
	},
  {
    'username': 'user5',
    'age': 127,
    'email': 'nicolasGravertt@hotmail.com'
	}
]);


// consultas SQL
// insertar a la coleccion objetos con campo status : inactivo
db.users.insertMany([
	{
    'username': 'user3',
    'age': 247,
    'email': 'nicolasGravertt@hotmail.com',
    'status': 'inactive'
	},
  {
    'username': 'user4',
    'age': 255,
    'email': 'nicolasGravertt@hotmail.com',
    'status': 'inactive'
	},
  {
    'username': 'user5',
    'age': 127,
    'email': 'nicolasGravertt@hotmail.com',
    'status': 'inactive'
	}
]);

// Obtener el usuario con username 'user7'

db.users.find({ // retorna un cursor
    username: 'user7'
});
// Retorna siempre 1
db.users.findOne({ // retorna un documento
    username: 'user7'
});

// Obtener los usuarios con edad mayor a 50 
db.users.find({ 
    age: { $gt:50 }
});

// $gt mayor que
// $gte mayor o igual que
// $lt menor que
// $lte menor o igual que

// Obtener la cantidad de usuarios con edad menor a 50 
// cursor -> count()
db.users.find({ 
    age: { $lt:50 }
}).count();

// obtener usuarios con una edad mayor a 50 y cuyo estatus sea activo
db.users.find({ 
    $and:[
        {age: { $gt:50 }},
        {status: 'active'}
    ]
});
