def status():
    from functools import reduce as rd
    ligado = True
    while ligado == True:
        lista = []
        escolha = input('''Escolha o modo:
            A = Adição
            S = Subtração
            M = Multiplicação
            D = Divisão
            Para sair precione qualquer outra tecla!''')
        if escolha == 'A':
            print('Você escolheu Adição')
            escolha_numeros = input('Escolha os numeros para serem Somados: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da soma dos numeros {lista} é: {sum(lista)}')
            lista.clear   
        elif escolha == 'S':
            print('Você escolheu Subtração')
            escolha_numeros = input('Escolha os numeros para serem Subtraidos: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da subtração dos numeros {escolha_numeros} é {rd(lambda x, y: x - y, lista)}')
            lista.clear
        elif escolha == 'M':
            print('Você escolheu Multiplicação')
            escolha_numeros = input('Escolha os numeros para serem Multiplicados: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da multiplicação dos numeros {escolha_numeros} é {rd(lambda x, y: x * y, lista)}')
            lista.clear
        elif escolha == 'D':
            print('Você escolheu Divisão')
            escolha_numeros = input('Escolha os numeros para serem Divididos: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da Divisão dos numeros {escolha_numeros} é {rd(lambda x, y: x / y, lista)}')
            lista.clear
        else:
            break
status()