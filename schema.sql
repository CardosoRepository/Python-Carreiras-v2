-- Criação da tabela de vagas
CREATE TABLE IF NOT EXISTS vagas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(250) NOT NULL,
    localidade VARCHAR(250) NOT NULL,
    salario INT,
    moeda VARCHAR(10),
    responsabilidades VARCHAR(2000)
);

-- Criação da tabela de inscrições
CREATE TABLE IF NOT EXISTS inscricoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vaga_id INT NOT NULL,
    nome VARCHAR(250) NOT NULL,
    email VARCHAR(300) NOT NULL,
    linkedin VARCHAR(500),
    experiencia VARCHAR(1000),
    FOREIGN KEY (vaga_id) REFERENCES vagas(id)
);
