from peewee import *
import os

arq = "meu_arquivo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Produto(BaseModel):
	nome = CharField()
	preco_custo = FloatField()
	preco_venda = FloatField()

class Venda(BaseModel):
	data = DateField()
	quantidade = IntegerField()
	produtos = ManyToManyField(Produto)

if __name__ == "__main__":

	if os.path.exists(arq):
			os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Produto, Venda, Produto.vendas.get_through_model()])

	except OperationalError as erro:
		print("erro")

	caneta = Produto.create(nome="caneta Bic", preco_custo=1.25, preco_venda=2.50)
	venda1 = Venda.create(data="2019-08-06", quantidade=4)
	caneta.vendas.add(caneta)

	print(venda1.data, venda1.quantidade)
	for i in venda1.produtos:
		print(i.nome, i.preco_custo, i.preco_venda)