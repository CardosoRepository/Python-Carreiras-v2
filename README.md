# Python-Carreiras-v2

Aplicação Flask que simula uma plataforma de visualização de vagas e candidaturas. Foco em boas práticas de backend com Python e integração com banco de dados SQLite.

---

## 🚀 Como rodar o projeto localmente

### ✅ Pré-requisitos

- Python 3.8+
- Git
- SQLite3
- (Recomendado) Ambiente virtual

---

### ⚙️ Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/python-carreiras-v2.git
cd python-carreiras-v2

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Crie o banco de dados SQLite
sqlite3 carreiras-python.db < schema.sql

# 5. Rode a aplicação Flask
flask --app app --debug run
