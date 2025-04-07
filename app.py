import os
from config import app
#from '''professor'''import rota 
#from '''aluno'' import rota
from turma.routes import turma

#app.register_blueprint(professor)
#app.register_blueprint(aluno)
app.register_blueprint(turma)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port= app.config['PORT'], debug=app.config['DEBUG'])

