import os
from peewee import *

arq = "marcenaria.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Cliente(BaseModel):
	nome = CharField()
	telefone = CharField()
	cpf = CharField()

class Material(BaseModel):
	descricao = CharField()
	preco = FloatField()
	fornecedor = CharField()

class Mobilia(BaseModel):
	descricao = CharField()
	preco = FloatField()
	materiais = ManyToManyField(Material)
	
class Pedido(BaseModel):
	preco_total = FloatField()
	cliente = ForeignKeyField(Cliente)

class Estoque(BaseModel):
	lista_material = ManyToManyField(Material)

if __name__ == "__main__":

	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Cliente, Material, Mobilia, Pedido, Estoque])

	except OperationError as erro:
		print("erro")