//Ordenação decrescente
db.usuarios.find(
  {
  $and: [
      {"sexo": /feminino/i},
      {"estado": {$eq: "Minas Gerais"}}
    ]
  }, 
  {"_id":0,"nome.primeiro":1, "sexo":1, "estado":1}
).sort({"nome.primeiro":-1})