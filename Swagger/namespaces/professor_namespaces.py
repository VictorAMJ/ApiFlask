from flask_restx import Namespace, Resource, fields
from professor.modelProfessor import model_create_professor, model_get_professor, model_get_professor_id, model_update_professor, model_delete_professor

professores_ns = Namespace("Professores", description="Operações relacionadas aos professores")

professores_input_model = professores_ns.model("Professor Input", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (AAAA-MM-DD)"),
    "materia": fields.String(required=True, description="Materia Ministrada"),
    "observacoes": fields.String(required=True, description="Observações gerais")
})

professores_output_model = professores_ns.model("Professor Output", {
    "id": fields.Integer(required=True, description="ID do professor"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (AAAA-MM-DD)"),
    "idade": fields.Integer(required=True, description="Idade do professor"),
    "materia": fields.String(required=True, description="Materia Ministrada"),
    "observacoes": fields.String(required=True, description="Observações gerais")
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self):
        return model_get_professor()
    
    @professores_ns.expect(professores_input_model)
    def post(self):
        data = professores_ns.payload
        response, status_code = model_create_professor(data)
        return response, status_code
    
@professores_ns.route("/<int:idprofessor>")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self, idprofessor):
        return model_get_professor_id(idprofessor)
    
    @professores_ns.expect(professores_input_model)
    def put(self, idprofessor):
        data = professores_ns.payload
        model_update_professor(idprofessor, data)
        return data, 200
    
    def delete(self, idprofessor):
        model_delete_professor(idprofessor)
        return{"mensagem":"Professor excluido com sucesso"}, 200
    