import flask
from flask import Flask, request

from webservice_banco import cadastro_bd

app = Flask('Serviço de Gerenciamento de cadastros')

@app.route('/', methods=['GET'])
def raiz():
    return {'mensagem': 'URL raiz do servidor, bem vindo!'}


@app.route('/cadastros', methods=['POST'])
def cadastrar_contato():
    contato = request.json

    if cadastro_bd.cadastrar(contato.get('cpf'), contato.get('telefone'), contato.get('nascimento')):
        return {}, 200

    else:
        return {}, 409


@app.route('/cadastros/<int:telefone>', methods=['DELETE'])
def remover_cadastro(telefone):
    if cadastro_bd.remover(telefone):
        return {}, 200
    else :
        return {}, 404


@app.route('/cadastros', methods=['PATCH'])
def recadastrar_cadastro():
    if cadastro_bd.recadastrar(request.json.get('novo_telefone'), request.json.get('id')):
        return {}, 200
    else:
        return {}, 404

@app.route('/cadastros', methods=['GET'])
def listar_cadastro():
    cadastros = cadastro_bd.listar()
    codigo = 200 if cadastros else 404

    return flask.jsonify(cadastros), codigo


@app.route('/cadastros/<int:cpf>', methods=['GET'])
def buscar_cpf(cpf):
    cadastro = cadastro_bd.buscar_por_cpf(cpf)
    codigo = 200 if cpf else 404

    return cadastro, codigo


def main():
    cadastro_bd.criar_banco()
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
