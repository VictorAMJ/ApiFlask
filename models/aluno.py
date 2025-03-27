dicionarioAluno = {
    "aluno": [{"nome":"lucas","id":15},
            {"nome":"cicero","id":29},
    ]
     
}

class AlunoNaoEncontrado(Exception):
    #raise "Aluno não foi encontrado!"
    pass

def add_aluno(novo_aluno):
    dicionarioAluno["aluno"].append(novo_aluno)
    
    if novo_aluno in dicionarioAluno:
        return "Aluno adicionado com sucesso!"
    raise AlunoNaoEncontrado


def lista_aluno():
    return dicionarioAluno["aluno"]


add_aluno("Victor")
lista_aluno()
#def lista_aluno_id(id)


