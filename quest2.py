from peewee import *
import os

arq = "meu_arquivo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Curso(BaseModel):
	nome = CharField()
	carga_horaria = IntegerField()
	escola = CharField()

class Habilidade(BaseModel):
	tipo_hab = CharField()

class CursoRealizado(BaseModel):
	curso = ForeignKeyField(Curso)
	habilidade = ForeignKeyField(Habilidade)
	ano_curso = IntegerField()

	def __str__(self):
		return str((self.curso.nome, self.curso.carga_horaria,
			self.curso.escola, self.habilidade.tipo_hab, 
			str(self.ano_curso)))

if __name__ == "__main__":

	if os.path.exists(arq):
			os.remove(arq)

	try: 
		db.connect()
		db.create_tables([Curso, Habilidade, CursoRealizado])

	except OperationalError as erro:
		print("erro")

	curso1 = Curso.create(nome="Introdução ao Linux", carga_horaria=60, escola="Microlins") 
	hab1 = Habilidade.create(tipo_hab="Operação de computador")
	curso_realizado = CursoRealizado.create(curso=curso1,habilidade=hab1, ano_curso=2018)
	todos = CursoRealizado.select()
	for i in todos:
		print(i)