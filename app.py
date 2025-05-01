from Swagger.swagger_config import configure_swagger
from config import app, db
from Professor.routesProfessor import professor
from Aluno.routesAluno import aluno
from Turma.routesTurma import turma


app.register_blueprint(professor)
app.register_blueprint(aluno)
app.register_blueprint(turma)

configure_swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port= app.config['PORT'], debug=app.config['DEBUG'])