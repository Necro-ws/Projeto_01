# Project 01

Este é o meu primeiro projeto utilizando o Git e Github

PT-BR

-Para este projeto estarei colocando um código em Python de uma calculadora bem simples mas que pretendo ir modificando ela em breve, somente para fins de estudo e aprender mais sobre a linguagem

 -Por enquanto é um projeto bem simples é um código em função utilizando condicionais, imputs, operadores logicos, relacionais, listas e modificações das mesmas.

 -O objetivo do codigo ate agora ele pega abre uma caixa de imput para a pessoa escolher o tipo de operação matematica que sera feita 
 -Quando o usuario escolhe o modo desta operação ele entra em uma condição de IF para que a pessoa possa colocar os numeros escolhidos para que eles sejam pegos deste imput e colocados em uma lista separada para que por meio dela seja feita a opereção e exibindo o resultado, e no final esta lista é zerada para que possa fazer mais contas do 0

 - Ainda pretendo mexer neste codigo para implementalo ou deixar melhor, mas como disse é somente para um fim de estudo e nada profissional ainda.

 - Primeira atualização

 Implementei a função reduce() para que o codigo fique mais limpo e de uma forma mais simples na hora de fazer as operações 
 ao inves de utilizar um looping for que era utilizado em sua antiga versão agora somente com um reduce posso colocar tudo na mesma linha de código
 Um exemplo: 

 lista = []
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

 antes eu tinha que utilizar um loop for para fazer a minha conta de subtração dos numeros coletados
 agora somente com uma linha de codigo utilizanto o reduce() e uma lambda eu consigo fazer isso 

 from functools import reduce as rd
 lista = []
 print('Você escolheu Subtração')
            escolha_numeros = input('Escolha os numeros para serem Subtraidos: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da subtração dos numeros {escolha_numeros} é {rd(lambda x, y: x - y, lista)}')
            lista.clear

assim o codigo ficando bem mais limpo para ser entendido e programado
pretendo fazer mais atualizações ainda.

 EN-US

This is my first project using Git and Github

 -For this project I will be putting in Python code for a very simple calculator but I intend to modify it soon, just for study purposes and to learn more about the language

  -For now it is a very simple project, it is a functional code using conditionals, inputs, logical operators, relationals, lists and modifications thereof.

  -The objective of the code so far is to open an input box for the person to choose the type of mathematical operation that will be performed
  -When the user chooses the mode of this operation, he enters an IF condition so that the person can enter the chosen numbers so that they are taken from this input and placed in a separate list so that the operation can be carried out through it and displaying the result, and at the end this list is reset so that you can do more calculations of 0

  - I still intend to change this code to implement it or make it better, but as I said it is only for study purposes and nothing professional yet.

  - First update

  I implemented the reduce() function so that the code is cleaner and simpler when carrying out operations.
  instead of using a for loop that was used in its old version, now only with a reduce can I put everything in the same line of code
  An example:

 lista = []
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

  Before I had to use a for loop to do my subtraction calculation of the collected numbers
  now with just one line of code using reduce() and a lambda I can do this

 from functools import reduce as rd
 lista = []
 print('Você escolheu Subtração')
            escolha_numeros = input('Escolha os numeros para serem Subtraidos: ')
            escolha_numeros = escolha_numeros.split(' ')
            for numero in escolha_numeros:
                lista.append(int(numero))
            print(f'O resultado da subtração dos numeros {escolha_numeros} é {rd(lambda x, y: x - y, lista)}')
            lista.clear

This way the code becomes much cleaner to be understood and programmed
I intend to make even more updates.

  