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

	except OperationalError as erro:
		print("erro")

	o1 = Ocorrencia.create(ocorrencia="dor de cabeça")
	o2 = Ocorrencia.create(ocorrencia="desanimo")
	r1 = Registro.create(data="2019-06-29", ocorrencia=o1, intensidade=0, observacao="jantei muito na noite anterior")
	r2 = Registro.create(data="2019-06-02", ocorrencia=o2, intensidade=1, observacao="desentendimento matianal")
	r3 = Registro.create(data="2019-06-09", ocorrencia=o1, intensidade=0, observacao="jantei na véspera")
	r4 = Registro.create(data="2019-06-01", ocorrencia=o2, intensidade=0, observacao="desânimo depois do almoço")
	r5 = Registro.create(data="2019-05-31", ocorrencia=o1, intensidade=1, observacao="janta pesada na noite anterior")
	print("ocorrrências")

	todas = Registro.select()
	for i in todas:
		print(i)
