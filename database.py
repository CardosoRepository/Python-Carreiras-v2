import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

string_conexao = os.getenv("db_conexao_string")
engine = create_engine(string_conexao)

def carrega_vagas_db():
	with engine.connect() as conn:
		resultado = conn.execute(text("select * from vagas"))
		vagas = []

		for vaga in resultado.all():
			vagas.append(vaga._asdict())
		
		return vagas
