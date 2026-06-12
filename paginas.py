# -*- coding: utf-8 -*-
"""
Título: Blueprint de Páginas - Lista Flask WEB II
Descrição: Blueprint responsável por renderizar os templates HTML da aplicação.
Data: 28/04/2026
"""
__author__ = "Nome Completo do Aluno"
__email__ = "aluno@fatec.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"

from flask import Blueprint, render_template

paginas = Blueprint("paginas", __name__, template_folder="templates")


@paginas.route("/")
def index():
    return render_template("paginas/index.html", title="Início")
