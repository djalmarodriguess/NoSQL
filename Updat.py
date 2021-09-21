//Update 
db.usuarios.updateOne({"nome.primeiro":"José"},
{
 $set: {"totconta": 100900, "profissao":"Programador" } 
}
)

//Update Many
db.usuarios.updateMany({"uf": "MG"},{$set:{"comida": "Pão de queijo"}})

//Replace One
db.usuarios.replaceOne({"nome.primeiro": "Adão"},{"Profissao": "Gerente","uf": "MG", "comida":"Pão de queijo" }
)
