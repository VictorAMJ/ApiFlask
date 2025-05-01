from . import api
from Swagger.namespaces.aluno_namespace import alunos_ns
from Swagger.namespaces.professor_namespaces import professores_ns
from Swagger.namespaces.turma_namespaces import turmas_ns

def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(alunos_ns, path="/aluno")
    api.add_namespace(professores_ns, path="/professor")
    api.add_namespace(turmas_ns, path="/turma")
    