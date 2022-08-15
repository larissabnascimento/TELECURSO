import sqlite3

ARQUIVO_BANCO = 'banco_de_dados_cadastro.db'

def criar_banco():
    with sqlite3.connect(ARQUIVO_BANCO) as conexao:
        conexao.execute('''
            create table if not exists contato (
                id integer primary key not null,
                cpf int unique not null,
                telefone int not null,
                nascimento date not null
            )
        ''')

def cadastrar(cpf, telefone, nascimento):
    try:
        with sqlite3.connect(ARQUIVO_BANCO) as conexao:
            cursor = conexao.execute('insert into cadastro (cpf, telefone, nascimento) values (?, ?, ?)',
                                     (cpf, telefone, nascimento))
            sucesso = cursor.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso

def remover(telefone):
    try:
        with sqlite3.connect(ARQUIVO_BANCO) as conexao:
            cursor = conexao.execute('delete from cadastro where telefone = ?', (telefone))
            sucesso = cursor.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso

def recadastrar(novo_telefone, id):
    try:
        with sqlite3.connect(ARQUIVO_BANCO) as conexao:
            cursor = conexao.execute('update cadastro set telefone = ? where id = ?', (novo_telefone, id))
            sucesso = cursor.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso

def listar():
    with sqlite3.connect(ARQUIVO_BANCO) as conexao:
        cursor = conexao.execute('select * from cadastro')
        tabela = cursor.fetchall()

    return tabela

def buscar_por_cpf(cpf):
    with sqlite3.connect(ARQUIVO_BANCO) as conexao:
        cursor = conexao.execute('select * from contato where cpf = ?', (cpf))
        linha = cursor.fetchone()

    return linha

