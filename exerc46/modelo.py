import os
from peewee import *

arq = "minha_saude.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Ocorrencia(BaseModel):
	ocorrencia = CharField()

class Registro(BaseModel):
	data = DateField()
	ocorrencia = ForeignKeyField(Ocorrencia)
	intensidade = IntegerField()
	observacao = CharField()

	def __str__(self):
		return str((str(self.data), self.ocorrencia, str(self.intensidade), self.observacao))

if __name__ == "__main__":

	if os.path.exists(arq):
		os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Ocorrencia, Registro])

	except OperationError as erro:
		print("erro")

	o1 = Ocorrencia.create(ocorrencia="dor de cabeça")
	r1 = Registro.create(data="2019-06-29", ocorrencia=o1, intensidade=0, observacao="jantei muito na noite anterior(resto de marmita do almoço)")
	print("teste ocorrência 1")

	todas = Registro.select()
	for i in todas:
		print(i)