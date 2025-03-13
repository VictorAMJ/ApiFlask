from flask import Flask, jsonify, request

app = Flask(__name__)


#PROFESSOR:

dicionarioProfessor = {
    "professores": [{
        "id": 1,
        "nome":"Caio",
        "idade": 27,
        "materia": "Desenvolvimento de APIs e Microsserviços",
        "observacoes": "Professor legal"
    }]
}

#criar:
@app.route("/professor", methods=["POST"])
def create_professor():
    dados = request.json
    dici_professores = dicionarioProfessor["professores"]
    for professor in dici_professores:
        if professor['id'] == dados['id']:
            return jsonify({'erro': 'ID já existe.'}), 400
        
    professor = {
        'id': dados['id'],
        'nome': dados['nome'],
        'idade': dados['idade'],
        'materia': dados['materia'],
        'observacoes': dados['observacoes']
    }

    dicionarioProfessor['professores'].append(professor)
    return jsonify(professor), 201

#ler
@app.route('/Professor', methods=['GET'])
def get_professor():
    dados = dicionarioProfessor['professores']
    return jsonify(dados)

#atualizar
@app.route('/Professor/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    dici_professores = dicionarioProfessor['professores']
    for professor in dici_professores:
        if professor['id'] == idProfessor:
            dados = request.json
            professor['id'] = dados['id']
            professor['nome'] = dados['nome']
            professor['idade'] = dados['idade']
            professor['materia'] = dados['materia']
            professor['observacoes'] = dados['observacoes']
            return jsonify(professor)
    
    return jsonify({'erro': 'Professor não encontrado'}), 404

#deletar
@app.route('/deletarProfessor/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    dici_professores = dicionarioProfessor['professores']
    for professor in dici_professores:
        if professor['id'] == idProfessor:
            dici_professores.remove(professor)
            return jsonify({'mensagem': 'Professor deletado com sucesso.'}), 200
    
    return jsonify({'erro': 'Professor não encontrado.'}), 404


#ALUNO:
dicionarioAluno = {
    'aluno': [{
        'id': 1,
        'nome': 'Jurema',
        'idede': 43,
        'turma_id':'ADS_3G', ### FAZER LIGAÇÃO COM O ID TURMA
        'data_nascimento':'15/06/1982',
        'nota_primeiro_semestre': 6.0,
        'nota_segundo_semestre': 8.0,
        'media_final': 7.0
    }]    
}

#criar
@app.route('/Aluno', methods=['POST'])
def create_aluno():
    dadosAluno = request.json
    dici_aluno = dicionarioAluno['aluno']
    for aluno in dici_aluno:
        if aluno['id'] == dadosAluno['id']:
            return jsonify({'erro': 'ID já existe.'}), 400
        
    aluno = {
        'id': dadosAluno['id'],
        'nome': dadosAluno['nome'],
        'idade': dadosAluno['idade'],
        'turma_id': dadosAluno['turma_id'],
        'data_nascimento': dadosAluno['data_nascimento'],
        'nota_primeiro_semestre': dadosAluno['nota_primeiro_semestre'],
        'nota_segundo_semestre': dadosAluno['nota_segundo_semestre'],
        'media_final': dadosAluno['media_final']
    }

    dicionarioAluno['aluno'].append(aluno)
    return jsonify(aluno), 201

#ler
@app.route('/Aluno', methods=['GET'])
def get_aluno():
    dadosAlunos = dicionarioAluno['aluno']
    return jsonify(dadosAlunos)

#atualizar

#deletar


#TURMA:
dicionarioTurma = {
    'turma' = [{
        "id": 1,
        "descricao": "nenhuma",
        "professor_id": 1, ### descobrir como faz a ligação com id do professor
        "ativo": True
    }]
}

#criar
@app.route('/Turma', methods=['POST'])
def create_turma():
    dadosTurma = request.json
    dici_turma = dicionarioTurma['turma']
    for turma in dici_turma:
        if turma["id"] == ["id"]:
            



if __name__=="__main__":
    app.run(debug=True)
