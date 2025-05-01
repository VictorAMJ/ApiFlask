from flask_restx import Namespace, Resource, fields
from Aluno.modelAluno import model_create_aluno, model_get_aluno, model_get_aluno_por_id, model_update_aluno, model_delete_aluno


alunos_ns = Namespace("Alunos", description="Operações relacionadas aos alunos")

alunos_input_model = alunos_ns.model("Aluno Input", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (AAAA-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada")
})

alunos_output_model = alunos_ns.model("Aluno Output", {
    "id": fields.Integer(required=True, description="ID do aluno"),
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (AAAA-MM-DD)"),
    "idade": fields.Integer(required=True, description="Idade do aluno"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "media_final": fields.Float(required=True, description="Media final do aluno"),
    
})


@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(alunos_output_model)
    def get(self):
        return model_get_aluno()
    
    @alunos_ns.expect(alunos_input_model)
    def post(self):
        data = alunos_ns.payload
        response, status_code = model_create_aluno(data)
        return response, status_code
    
@alunos_ns.route("/<int:idAluno>")
class AlunosIdResource(Resource):
    @alunos_ns.marshal_list_with(alunos_output_model)
    def get(self, idAluno):
        return model_get_aluno_por_id(idAluno)
    
    @alunos_ns.expect(alunos_input_model)
    def put(self, idAluno):
        data = alunos_ns.payload
        model_update_aluno(idAluno, data)
        return data, 200
    
    def delete(self, idAluno):
        model_delete_aluno(idAluno)
        return{"mensagem":"Aluno excluido com sucesso"}, 200
    