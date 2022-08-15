import requests

URL_PREFIXO = 'http://localhost:8080'

def criar_sessao():
    s = requests.session()

    return s

def ler():
    cpf = int(input('Digite o nnúmero do seu CPF: '))
    telefone = int(input('Digite o telefone: '))
    nascimento = input('Digite a data de nascimento (aaaa-mm-dd): ')

    return {
        'CPF': cpf,
        'telefone': telefone,
        'nascimento': nascimento
    }

def imprimir(cadastro):
    print('#')
    print('ID:', cadastro['id'])
    print('CPF:', cadastro['cpf'])
    print('Telefone:', cadastro['telefone'])
    print('Data de Nascimento:', cadastro['nascimento'])