from peewee import *
import os

arq = "meu_arquivo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Exame(BaseModel):
	nome = CharField()
	preco = FloatField()
	prazo_dias = IntegerField()

class Requisicao(BaseModel):
	nome = CharField()

class RequisicaoDoExame(BaseModel):
	data_pedido_exame = DateField()
	nome_paciente = CharField()
	nome_medico = CharField()
	exame = ForeignKeyField(Exame)
	requisicao = ForeignKeyField(Requisicao)

	def __str__(self):
		return str((str(self.data_pedido_exame), self.nome_paciente, self.nome_medico, str(self.exame.preco), str(self.exame.prazo_dias), self.exame.nome, self.requisicao.nome))

if __name__ == "__main__":
	
	if os.path.exists(arq):
		os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Exame, Requisicao, RequisicaoDoExame])

	except OperationalError as erro:
		print("erro")

	exame1 = Exame.create(nome="triglicerídeos", preco=35.0, prazo_dias=10)
	requisicao1 = Requisicao.create(nome="req 1")
	req_exame = RequisicaoDoExame.create(data_pedido_exame="2019-07-11", nome_paciente="Nathalia Kanis", nome_medico="Guilherme Panosso", exame=exame1, requisicao=requisicao1)
	todos = req_exame.select()
	for i in todos:
		print(i)