from peewee import *
import os

arq = "meu_arquivo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Planta(BaseModel):
	nome = CharField()
	nome_cientifico = CharField()
	tamanho_folha = CharField()

class Jardim(BaseModel):
	nome = CharField()
	plantas = ManyToManyField(Planta)

if __name__ == "__main__":
	
	if os.path.exists(arq):
		os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Planta, Jardim, Planta.jardims.get_through_model()])

	except OperationalError as erro:
		print("erro")

	planta1 = Planta.create(nome="margarida", nome_cientifico="lolapalusa", tamanho_folha="pequena")
	jardim1 = Jardim.create(nome="jardim dos sonhos")
	planta1.jardims.add(planta1)
	print(jardim1.nome)
	for i in jardim1.plantas:
		print(i.nome, i.nome_cientifico, i.tamanho_folha)
