def status():
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
                resultado_sub = lista[0]
                for numero_lista_sub in range(1, len(lista)):
                    resultado_sub -= lista[numero_lista_sub]
            print(f'O resultado da subtração dos numeros {lista} é: {resultado_sub}')
            lista.clear
        elif escolha == 'M':
            print('Você escolheu Multiplicação')
            escolha_numeros = input('Escolha os numeros para serem Multiplicados: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
                resultado_mult = lista[0]
                for numero_lista_mult in range(1, len(lista)):
                    resultado_mult *= lista[numero_lista_mult]
            print(f'O resultado da subtração dos numeros {lista} é: {resultado_mult}')
            lista.clear
        elif escolha == 'D':
            print('Você escolheu Divisão')
            escolha_numeros = input('Escolha os numeros para serem Divididos: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
                resultado_div = lista[0]
                for numero_lista_div in range(1, len(lista)):
                    resultado_div /= lista[numero_lista_div]
            print(f'O resultado da subtração dos numeros {lista} é: {resultado_div}')
            lista.clear
        else:
            break
status()
