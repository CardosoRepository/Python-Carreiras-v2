from sqlalchemy import create_engine

string_conexao = 'mysql+pymysql://root:123456@127.0.0.1:3306/carreira_python?charset=utf8mb4'
engine = create_engine(string_conexao)

with engine.connect() as conn:
  resultado = conn.execute(text("select * from vagas"))
  print(resultado.all())
