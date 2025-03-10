from flask import Flask, jsonify, request

dicionario = {
    'professores': [{
        'id': 1,
        'nome':'Caio',
        'idade': 27,
        'materia': 'Desenvolvimento de APIs e Microsserviços',
        'observacoes': 'Professor legal'
    }]
}



rota_professor = Flask(__name__)

#criar:
@rota_professor.route('/criarProfessor', methods=['POST'])
def create_professor():
    dados = request.json
    dici_professores = dicionario['professores']
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

    dicionario['professores'].append(professor)
    return jsonify(professor), 201


#ler
@rota_professor.route('/lerProfessor', methods=['GET'])
def get_professor():
    dados = dicionario['professores']
    return jsonify(dados)


#atualizar
@rota_professor.route('/atualizarProfessor/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    dici_professores = dicionario['professores']
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
@rota_professor.route('/deletarProfessor/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    dici_professores = dicionario['professores']
    for professor in dici_professores:
        if professor['id'] == idProfessor:
            dici_professores.remove(professor)
            return jsonify({'mensagem': 'Professor deletado com sucesso.'}), 200
    
    return jsonify({'erro': 'Professor não encontrado.'}), 404


if __name__=="__main__":
    rota_professor.run(debug=True)

