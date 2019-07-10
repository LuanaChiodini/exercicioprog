class Doacao(BaseModel):
	data = DataField()
	item = CharField()
	tipo_destinatario = ForeignKeyField(TipoDeDestinatario)
	observacao = CharField()

	def __str__(self):
		return str((str(self.data), self.item, self.tipo_destinatario, self.observacao))

class TipoDeDestinatario(BaseModel):
	tipo_destinatario = CharField()

juridico = TipoDeDestinatario.create(tipo_destinatario="Pessoa Jurídica")
doacao1 = Doacao.create(data="2019-03-01", item="bicicleta", tipo_destinatario=juridico, observacao="Vizinho Invan")
todos = Doacao.select()
for i in todos:
	print(i)

class Local(BaseModel):
	nome = CharField()

class Atividade(BaseModel):
	nome = CharField()

class AtividadeNoLocal(BaseModel):
	local = ForeignKeyField(Local)
	atividade = ForeignKeyField(Atividade)
	data = DateField()

	def __str__(self):
		return str((self.local, self.atividade, str(self.data))

local1 = Local.create(nome="Itaunas")
atividade1 = Atividade.create(nome="Praia")
evento = AtividadeNoLocal(local=local1, atividade=atividade1, data="2018-05-24")
todos = AtividadeNoLocal.select()
for i in todos:
	print(i)
