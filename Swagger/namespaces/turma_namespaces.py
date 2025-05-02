from flask_restx import Namespace, Resource, fields
from turma.modelTurma import model_create_turma, model_get_turma, model_get_turma_por_id, model_update_turma, model_delete_turma

turmas_ns = Namespace("Turmas", description="Operações relacionadas as turmas")

turma_input_model = turmas_ns.model("Turma Input", {
    "descricao": fields.String(required=True, description="Descrição da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor associada"),
    "ativo": fields.Boolean(required=True, description="Estado que a turma se encontra")
})

turma_output_model = turmas_ns.model("Turma Output", {
    "id": fields.Integer(required=True, description="ID da turma"),
    "descricao": fields.String(required=True, description="Descrição da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor associada"),
    "ativo": fields.Boolean(required=True, description="Estado que a turma se encontra")
})


@turmas_ns.route("/")
class TurmaResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    def get(self):
        return model_get_turma()
    
    @turmas_ns.expect(turma_input_model)
    def post(self):
        dadosTurma = turmas_ns.payload
        response, status_code = model_create_turma(dadosTurma)
        return response, status_code
    
@turmas_ns.route("/<int:idturma>")
class TurmaIDResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    def get(self, idturma):
        return model_get_turma_por_id(idturma)
    
    @turmas_ns.expect(turma_input_model)
    def put(self, idturma):
        data = turmas_ns.payload
        model_update_turma(idturma, data)
        return data, 200
    
    def delete(self, idturma):
        model_delete_turma(idturma)
        return{"mensagem":"Turma excluida com sucesso"}, 200
