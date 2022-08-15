import cadastro_aluno

def main():
    sessao = cadastro_aluno.criar_sessao()

    while True:
        print('-' * 40)
        print('0 - Sair do programa')
        print('1 - Cadastrar um novo CPF')
        print('2 - Remover um cadastro a partir do telefone')
        print('3 - Recadastrar os dados do cadastro a partir do identificador')
        print('4 - Listar todos os cadastros')
        print('5 - Mostrar cadastros a partir de seu CPF')
        opcao = int(input('Escolha sua opção: '))

        if opcao == 0:
            print('Saindo do programa...')
            break
        elif opcao == 1:
            with sessao.post(cadastro_aluno.URL_PREFIXO + '/contatos', json=cadastro_aluno()) as resposta:
                if resposta.status_code == 201:
                    print('Cadastro adicionado com sucesso!')
                else:
                    print('Não foi posssível adicionar cadastro:', resposta.status_code)
        elif opcao == 2:
            telefone = int(input('Digite o telefone a ser removido: '))

            with sessao.delete(cadastro_aluno.URL_PREFIXO + f'/cadastro/{telefone}') as resposta:
                if resposta.status_code == 200:
                    print('Cadastro removido com sucesso!')
                else:
                    print('Não foi possível remover o cadastro:', resposta.status_code) 
        elif opcao == 3:
            dados = {
                'id': int(input('Digite o identificador do cadastro: ')),
                'novo_telefone': int(input('Digite o novo telefone do cadastro: '))
            }

            with sessao.patch(cadastro_aluno.URL_PREFIXO + '/cadastro', json=dados) as resposta:
                if resposta.status_code == 200:
                    print('Contato atualizado com sucesso!')
                else:
                    print('Não foi possível atualizar o cadastro:', resposta.status_code)
        elif opcao == 4:
            with sessao.get(cadastro_aluno.URL_PREFIXO + '/cadastros') as resposta:
                if resposta.status_code == 200:
                    for aluno in resposta.json():
                        cadastro_aluno.imprimir(aluno)
                else:
                    print('Nenhum cadastro encontrado:', resposta.status_code)

        elif opcao == 5:
            cpf = int(input('Digite o CPF: '))

            with sessao.get(cadastro_aluno.URL_PREFIXO + f'/cadastros/{cpf}') as resposta:
                if resposta.status_code == 200:
                    cadastro_aluno.imprimir(resposta.json())
                else:
                    print('CPF não encontrado:', resposta.status_code)

        else:
            print('Opção inválida, tente novamente!')


if __name__ == '__main__':
    main()
