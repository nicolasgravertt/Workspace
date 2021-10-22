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

// $gt mayor que >
// $gte mayor o igual que >=
// $lt menor que <
// $lte menor o igual que <=
// ne no es igual a !=

// Obtener la cantidad de usuarios con edad menor a 50 
// cursor -> count()
db.users.find({ 
    age: { $lt:50 }
}).count();

// obtener usuarios con una edad mayor a 50 y cuyo status sea activo
db.users.find({ 
    $and:[
        {age: { $gt:50 }},
        {status: 'active'}
    ]
});

// obtener todos los usuarios cuya edad sea distinta a 247
db.users.find({ 
    age: {$ne:247}
});

// obtener todos los usuarios que tengan por edad: 255 o 247 o 127
// primera opcion.
db.users.find({ 
    $or:[{age:255},
        {age:247},
        {age:127}
    ]
});
// segunda forma
db.users.find({ 
    age: {$in:[255,247,127]}
});

// Obtener solo los usuarios que contengan el atributo status
db.users.find({ 
    status: {$exists:true}
});

// Obtener solo los usuarios que NO contengan el atributo status
db.users.find({ 
    status: {$exists:false}
});

// obtener los usuarios con status activo
// primera forma
db.users.find({ 
    $and:[{status: {$exists:true}},
        {status:'active'}
    ]
});
// segunda forma
db.users.find({ 
    status:'active'
});

// Obtener todos los usuarios con status activo y correo electronico
db.users.find({ 
    $and:[{status: {$exists:true}},
        {status:'active'},
        {email: {$exists:true}}
    ]
});

// Obtener el usuario con mayor edad
// cursor.sort() ordenar ascendente o descendente
// cursor.limit() Limita la cantidad de datos a devolver por consulta
db.users.find().sort(
    {
        age: -1 // asc : 1 desc: -1
    }
).limit(1);

// Obtener 3 usuarios mas jovenes
db.users.find().sort(
    {
        age: 1 // asc : 1 desc: -1
    }
).limit(3);

// Usuarios que su correo termine con .com
db.users.find({
    email: /.com$/ // algo equivalente a like en bd relacionales.
});

// Usuarios que su correo comience con nica
db.users.find({
    email: /^nica/ // algo equivalente a like en bd relacionales.
});

// Usuarios que su correo tenga con hola
db.users.find({
    email: /hola/ // algo equivalente a like en bd relacionales.
});

// Al metodo find se le puede entregar un segundo {} para indicarle que atributos queremos obtener de la consulta
db.users.find({ 
    status:'active'
},{
    _id: false,
    age: true
}
);

//Actualizar datos

db.users.updateOne(
    {
        _id: ObjectId("6172bf2983e3ee308a9489b8") // where id = ...
    },
    {
        $set:{
            username: 'cody' // set username = ...
        }
    }
);

db.users.updateMany(
    {
        age: 255
    },
    {
        $set:{
            username: 'cody' // set username = ...
        }
    }
);

//Actualizar datos

db.users.updateOne(
    {
        _id: ObjectId("6172bf2983e3ee308a9489b8") // where id = ...
    },
    {
        $set:{
            username: 'cody', // set username = ...
            profile_picture: 'www.codigofacilito.com/user1' // al no existir se agrega el campo
        }
    }
);

db.users.updateOne(
    {
        _id: ObjectId("6172bf2983e3ee308a9489b8") // where id = ...
    },
    {
        $unset:{
            profile_picture: 'www.codigofacilito.com/user1' // se quita el campo con $unset:
        }
    }
);

db.users.updateMany(
    {
    },
    {
        $inc:{ // incrementar la edad en 1 para todos los registros $inc:
            age: 1
        }
    }
);

// eliminar documentos

db.users.remove({
    status: 'inactive'
});

/* 
    Para viajar entre documentos embebidos con notacion
    'usuario.direccion'
    Para buscar dentro de una lista en find.
    $elemMatch: 
    db.users.drop(); Para eliminar la coleccion de datos.
    db.dropDatabase(); Eliminar la bd.
    mongodump --db prueba // crea respaldo o backup de la base de datos.
    mongorestore --db prueba dump/prueba // se restaura la base de datos. 
*/
