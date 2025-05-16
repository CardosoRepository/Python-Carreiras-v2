import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

string_conexao = os.getenv("db_conexao_string")
engine = create_engine(string_conexao)

# Executa o schema.sql
def cria_tabelas():
    with engine.connect() as conn:
        with open('schema.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()

        comandos = [comando.strip() for comando in sql_script.split(';') if comando.strip()]
        for comando in comandos:
            conn.execute(text(comando))

			
def carrega_vagas_db():
	with engine.connect() as conn:
		resultado = conn.execute(text("select * from vagas"))
		vagas = []

		for vaga in resultado.all():
			vagas.append(vaga._asdict())
		
		return vagas

def carrega_vaga_db(id):
	with engine.connect() as conn:
		resultado = conn.execute(text(
			f"SELECT * FROM vagas WHERE id = :val"
        ),
            { 'val': id }
        )
		registro = resultado.mappings().all()
		
		if len(registro) == 0:
			return None
		else:
			return dict(registro[0])
		
def adiciona_inscricao(id_vaga, dados):
	with engine.begin() as conn:
		query = text("""
			INSERT INTO inscricoes (vaga_id, nome, email, linkedin, experiencia)
			VALUES (:vaga_id, :nome, :email, :linkedin, :experiencia)
		""")
		conn.execute(
			query, {
				'vaga_id': id_vaga,
				'nome': dados['nome'],
				'email': dados['email'],
				'linkedin': dados['linkedin'],
				'experiencia': dados['experiencia']
            }
        )