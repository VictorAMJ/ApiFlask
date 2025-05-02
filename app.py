from Swagger.swagger_config import configure_swagger
from config import app, db
from professor.routesProfessor import professor
from aluno.routesAluno import aluno
from turma.routesTurma import turma


app.register_blueprint(professor)
app.register_blueprint(aluno)
app.register_blueprint(turma)

configure_swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port= app.config['PORT'], debug=app.config['DEBUG'])