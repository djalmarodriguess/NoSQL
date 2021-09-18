//Somente idade
db.usuarios.find({},{"_id":0, "idade":1})

//Somente idade maior que 18
db.usuarios.find(
  {"idade": {$gt: 18}}, 
  {"_id":0, "idade":1, "nome.primeiro":1}
)

//Idade maior ou igual a 25
db.usuarios.find(
  {"idade": {$gte: 25}},
  {"_id":0, "idade": 1, "nome.primeiro":1}
)

//Totconta maior que 20000
db.usuarios.find(
  {"totconta":{$gt:20000}},
  {"_id":0}
  )

//Totconta maior ou igual a 20000 E sexo masculino
db.usuarios.find( { $and: [
  {"totconta": {$gte: 20000}},
  {"sexo": /masculino/i}
  ]
})

//Sexo Feminino E uf = MG
db.usuarios.find({$and:[
  {"sexo": /feminino/i},
  {"uf": {$eq: "MG"}}
  ]
},
  {"_id":0, "nome.primeiro":1, "uf":1, "sexo":1}
)

//Atlético Mineiro OU São Paulo
db.usuarios.find({$or:[
  {"time":{$eq:"Atlético Mineiro"}},
  {"time":{$eq: "São Paulo" }}

]},
{"_id":0, "time":1, "nome.primeiro":1}
) 

//Sobrenome ou Nome Araújo E totconta maior que 150000
db.usuarios.find({ 
  $and: [
  {
      "totconta": {$gte: 15750}
  }, 
  { $or: [
    {"nome.sobrenome": "Araújo"},
    {"nome.primeiro": "Aráujo"}
    ]
  }
]
})