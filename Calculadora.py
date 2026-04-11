#Projeto de um sistema de calculadora para realização de operações
#A logica por trás é apenas realizar calculos das 4 operações basicas, soma, subtração, multiplicação e divisão

print('Bem vindo!')
#O loop de while True serve para manter a calculadora em funcionamento e assim poder realizar varias operações seguidas
while True:
    #O comando try é um comando feito para verificar o funcionamento do codigo ao longo dele
    #Nesse caso aqui ele serve para verificar se o usuario está realmente digitando valores nas entradas das variaveis X e Y
    try:
        X = float(input('Digite o primeiro valor \n'))
        Y = float(input('Digite o segundo valor \n'))
        #Se o codigo chegou nessa parte é porque o usuario digitou valores numericos para as duas variaveis
        operador = input('Escolha a operação a ser realizada, Digite:\n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\nexit para sair\n')
        #Após a escolha do operador entramos numa cadeia de ifs, onde será realizada a operação deseja ou o encerramento do funcionamento do codigo
        if operador == '+':
            valor = X+Y
            print(f'Esse é o resultado da soma: {valor:.2f}')
        elif operador == '-':
            valor = X-Y
            print(f'Esse é o resultado da subtração: {valor:.2f}')
        elif operador == '*':
            valor = X*Y
            print(f'Esse é o resultado da multiplicação: {valor:.2f}')
        elif operador == '/':
            #Essa cadeia de condicional alinhada serve para caso onde o usuario tente fazer divisão por 0 e o codigo não falhe
            if X == 0  and Y == 0:
                print('Indeterminação')
            elif Y == 0:
                print('Indefinido')
            else:
                valor = X/Y
                print(f'Esse é o resultado da divisão {valor:.2f}')
        elif operador == 'exit':
            print('Obrigado por usar nossa calculadora')
            break
        else:
            #O else está aqui para caso o usuario use um operador que não seja alguma das opções oferecidas
            print('Esse é um operador invalido, por favor tente novamente!')
    except ValueError:
        print('ERRO! digite um valores validos para as opções')
        #Se o codigo chega no except é devido ao usuario não ter digitado um numero em alguma das duas variaveis 