# -*- coding: utf-8 -*-
"""
Título: Criação de Rotas Simples - Lista Flask WEB II
Descrição: Blueprint com todas as rotas dos exercícios de criação de rotas simples.
Data: 30/05/2026
"""
__author__ = "Nome Completo do Aluno"
__email__ = "aluno@fatec.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"

from flask import Blueprint, request, jsonify

rotas = Blueprint("rotas", __name__)

# --- Exercício 1 ---
@rotas.route("/message")
def message():
    return "Cadastro Salvo com sucesso", 200


# --- Exercício 2 ---
STATUS_MESSAGES = {
    200: "200 OK: Sucesso geral.",
    201: "201 Created: Sucesso na criação.",
    400: "400 Bad Request: Erro do cliente (sintaxe).",
    401: "401 Unauthorized: Falta autenticação.",
    404: "404 Not Found: Recurso não encontrado.",
    500: "500 Internal Server Error: Erro no servidor.",
}

@rotas.route("/message/<int:status>")
def message_status(status):
    msg = STATUS_MESSAGES.get(status)
    if msg:
        return msg, status
    return "Status desconhecido.", 400


# --- Exercício 3 ---
@rotas.route("/auth/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario", "")
    senha = request.form.get("senha", "")
    if usuario == "genivaldo" and senha == "jerusa":
        return jsonify({"status": 200, "mensagem": "200 OK: Sucesso geral."}), 200
    return jsonify({"status": 401, "mensagem": "401 Unauthorized: Falta autenticação."}), 401


# --- Exercício 4 ---
def _validar_cpf(cpf: str) -> bool:
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    # Primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
    if digito1 != int(cpf[9]):
        return False
    # Segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
    return digito2 == int(cpf[10])

@rotas.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    nome = request.form.get("nome", "")
    cpf = request.form.get("cpf", "")
    if not nome or not cpf:
        return jsonify({"status": 400, "mensagem": "400 Bad Request: Erro do cliente (sintaxe)."}), 400
    if _validar_cpf(cpf):
        return jsonify({"status": 201, "mensagem": "201 Created: Sucesso na criação."}), 201
    return jsonify({"status": 400, "mensagem": "400 Bad Request: Erro do cliente (sintaxe)."}), 400


# --- Exercício 5: ---
@rotas.route("/convert/celsius/<float:temp>")
def converter_celsius(temp):
    fahrenheit = temp * 1.8 + 32
    return jsonify({"celsius": temp, "fahrenheit": round(fahrenheit, 2)}), 200


# --- Exercício 6: ---
@rotas.route("/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"status": 400, "mensagem": "400 Bad Request: Erro do cliente (sintaxe)."}), 400
    return jsonify({"status": 200, "mensagem": f"Você pesquisou por: {q}"}), 200


# --- Exercício 7 ---
@rotas.route("/api/register", methods=["POST"])
def register():
    nome = request.form.get("nome", "")
    try:
        idade = int(request.form.get("idade", -1))
    except ValueError:
        return jsonify({"status": 400, "mensagem": "400 Bad Request: Erro do cliente (sintaxe)."}), 400
    if idade < 18:
        return jsonify({"erro": "Cadastro permitido apenas para maiores de idade"}), 403
    return jsonify({"status": 201, "mensagem": f"Usuário {nome} cadastrado"}), 201


# --- Exercício 8 ---
PRODUTOS = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 249.90},
    {"id": 2, "nome": "Mouse Gamer",      "preco": 159.90},
    {"id": 3, "nome": "Monitor 24\"",     "preco": 1299.00},
]

@rotas.route("/products")
def products():
    if not PRODUTOS:
        return "", 204
    return jsonify(PRODUTOS), 200


# --- Exercício 9 ---
@rotas.route("/admin/dashboard")
def admin_dashboard():
    api_key = request.headers.get("X-Api-Key")
    if api_key == "secret123":
        return jsonify({"status": 200, "mensagem": "Acesso ao painel administrativo liberado"}), 200
    return jsonify({"status": 401, "mensagem": "401 Unauthorized: Falta autenticação."}), 401
