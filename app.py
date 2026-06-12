# -*- coding: utf-8 -*-
"""
Titulo: App principal - Lista Flask WEB II
Descricao: Cria a aplicacao e registra as blueprints.
Data: 28/04/2026
"""
__author__ = "Nome Erica Crepaldi"
__email__ = "erica.crepaldi@aluno.cps.sp.gov.br"
__turma__ = "DSM - 2 Semestre / Noturno"
__version__ = "1.0.0"



from flask import Flask
from rotas import rotas
from paginas import paginas

app = Flask(__name__)
app.register_blueprint(rotas)
app.register_blueprint(paginas)

if __name__ == "__main__":
    app.run(debug=True)
