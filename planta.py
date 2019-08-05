from peewee import *
import os

arq = "meu_arquivo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Planta(BaseModel):
	nome_planta = CharField()

class Jardim(BaseModel):
	nome_jardim = CharField()

class PlantaDoJardim(BaseModel):
	planta = ForeignKeyField(Planta)
	jardim = ForeignKeyField(Jardim)
	nome_cientifico = CharField()
	tamanho_folha = CharField()

	def __str__(self):
		return str(self.planta.nome_planta) + " " + str(self.jardim.nome_jardim) + " " + self.nome_cientifico + " " + self.tamanho_folha

if __name__ == "__main__":
	
	if os.path.exists(arq):
		os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Planta, Jardim, PlantaDoJardim])

	except OperationalError as erro:
		print("erro")

	planta1 = Planta.create(nome_planta="nathalia")
	jardim1 = Jardim.create(nome_jardim="panossol")
	terreno = PlantaDoJardim.create(planta=planta1, jardim=jardim1, nome_cientifico="kanissi panissi", tamanho_folha="pequena")
	todos = PlantaDoJardim.select()
	for i in todos:
		print(i)
