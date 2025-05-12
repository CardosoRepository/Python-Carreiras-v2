import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

string_conexao = os.getenv("db_conexao_string")
engine = create_engine(string_conexao)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS vagas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(250) NOT NULL,
            localidade VARCHAR(250) NOT NULL,
            salario INT,
            moeda VARCHAR(10),
            responsabilidades VARCHAR(2000)
        )
    """))
	
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