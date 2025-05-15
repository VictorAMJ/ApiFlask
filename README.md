# 🖥️ API Principal: Gestão Escolar 📕

Este repositório contém a **API de Gestão Escolar**, desenvolvida em **Flask** e **SQLAlchemy**, sendo a parte principal do nosso projeto que tem o objetivo de ser um sistema onde administra e organiza alunos, professores e turmas de uma instituição de ensino.

⚠️ **Esta API funciona de forma independente, porém para funcionar de forma completa com todos seus atributos é necessário utilizar também as APIs "Reserva_Salas" e "Atividades_Escolares"**


## 🔧 Ferramentas Utilizadas

- Python 3
- Flask
- SQLAlchemy
- SQLite (Bando de dados local)
- Requests
- Swagger
- Docker
- Unittest

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ApiFlak.git
cd ApiFlak
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:8080`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

#### Aluno:
- `GET /aluno` – Lista todas os alunos
- `POST /aluno` – Cria um novo aluno
- `GET /aluno/<id>` – Retorna os dados de um aluno específico
- `PUT /aluno/<id>` –  Atualiza os dados de um aluno
- `DELETE /aluno/<id>` – Deleta um aluno existente

#### Professor:
- `GET /professor` – Lista todas os professores
- `POST /professor` – Cria um novo profesor
- `GET /professor/<id>` – Retorna os dados de um professor específico
- `PUT /professor/<id>` –  Atualiza os dados de um professor
- `DELETE /professor/<id>` – Deleta um professor existente

#### Turma:
- `GET /turma` – Lista todas as turmas
- `POST /turma` – Cria um nova turma
- `GET /turma/<id>` – Retorna os dados de uma turma específica
- `PUT /turma/<id>` –  Atualiza os dados de uma turma
- `DELETE /turma/<id>` – Deleta uma turma existente

⚠️ **Os exemplos de corpo JSON estão no Swagger, acesse e crie, transforme e remodele como quiser.**

## 🧑‍💻 Autores

Gabriela Araujo Rodrigues
Victor Alexandre Martuzzo de Jesus
Yara Castro Lima