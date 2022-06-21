opção = 0
dadosCli = []
# menu
while opção!= 5:
    print(''' LOJA VICTORIA
[ 1 ] Cadastrar cliente
[ 2 ] Adicionar endereço
[ 3 ] Mostrar dados
[ 4 ] Mostrar clientes
[ 5 ] Sair do programa ''')
    opção = int(input('Digite uma opção: '))

    # cadastrar cliente
    if opção == 1:
        dados = {}
        dados['---Cliente: '] = str(input('Digite o nome completo do cliente: ')).lower()
        dados['---Loguin: '] = str(input('Crie um loguin: ')).lower()
        dados['---Senha: '] = int(input('Crie uma senha (apenas números): '))
        dados['---Email: '] = str(input('Digite seu email: ')).lower()
        dados['---Data de nascimento: '] = str(input('Digite sua data de nascimento: '))
        dados['---Número de celular: '] = int(input('Digite seu número de celular: '))
        dadosCli.append(dados)
        print(dadosCli)

    # cadastrar endereço
    elif opção == 2:
        endereço = {}
        endereço['---Nome da cidade: '] = str(input('Nome da cidade: ')).lower()
        endereço['---Nome do bairro: '] = str(input('Nome do bairro: ')).lower()
        endereço['---Nome da rua: '] = str(input('Nome da rua: ')).lower()
        endereço['---Número da casa/apartamento: '] = int(input("Número da casa/apartamento: "))
        endereço['---Ponto de referência: '] = str(input('Ponto de referência: ')).lower()
        dadosCli.append(endereço)
        print(dadosCli)

# mostrar dados
    elif opção == 3:
        loguin = input('Digite o loguin do usuário desejado: ')
        for i in dadosCli:
            if i['---Loguin: '] == loguin:
                print(i)
        else:
            print('Esse usuário não existe')

    # mostrar clientes // nao consegui que mostrasse o endereço junto
    elif opção == 4:
        for j in dadosCli:
            print(j['---Cliente: '])

    # finalizar programa
    elif opção == 5:
        print('Ok :( Finalizando...')

    # opção inexistente
    else:
        print('A opção é inválida :/ Tente novamente!')

    print('-' * 100)

print('Fim do programa! Volte sempre :)')