#Projeto de um sistema de calculadora para realização de operações
#A logica por trás é apenas realizar calculos das 4 operações basicas, soma, subtração, multiplicação e divisão

print('Bem vindo!')
#O loop de while True serve para manter a calculadora em funcionamento e assim poder realizar varias operações seguidas
list_historico = []
while True:
    #O comando try é um comando feito para verificar o funcionamento do codigo ao longo dele
    #Nesse caso aqui ele serve para verificar se o usuario está realmente digitando valores nas entradas das variaveis X e Y
    try:
        entrada = input("Digite a expressão a ser calculada no seguinte formato X + Y, tendo como opção as seguintes operações:\n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\nDigite:\nhist para ver o historico de operações ou exit para sair\n")
        #Após a escolha do operador entramos numa cadeia de ifs, onde será realizada a operação deseja ou o encerramento do funcionamento do codigo
        if entrada == 'exit':
            print('Obrigado por usar nossa calculadora')
            break
        elif entrada == 'hist':
            for i, conta in enumerate(list_historico):
                print(f'{i+1}. {conta}')
        else:
            entrada =  entrada.split()
            X = float(entrada[0])
            operador = str(entrada[1])
            Y = float(entrada[2])
            if operador == '+':
                valor = X+Y
                operação_historico = str(f'{X} + {Y} = {valor:.2f}')
                print(f'Esse é o resultado da soma: {valor:.2f}')
                list_historico.append(operação_historico)
            elif operador == '-':
                valor = X-Y
                operação_historico = str(f'{X} - {Y} = {valor:.2f}')
                print(f'Esse é o resultado da subtração: {valor:.2f}')
                list_historico.append(operação_historico)
            elif operador == '*':
                valor = X*Y
                operação_historico = str(f'{X} x {Y} = {valor:.2f}')
                print(f'Esse é o resultado da multiplicação: {valor:.2f}')
                list_historico.append(operação_historico)
            elif operador == '/':
                #Essa cadeia de condicional alinhada serve para caso onde o usuario tente fazer divisão por 0 e o codigo não falhe
                if X == 0  and Y == 0:
                    operação_historico = str('0/0 = Indeterminação')
                    print('Indeterminação \n')
                    list_historico.append(operação_historico)
                elif Y == 0:
                    operação_historico = str(f'{X}/0 = Indefinido')
                    print('Indefinido \n')
                    list_historico.append(operação_historico)
                else:
                    valor = X/Y
                    operação_historico = str(f'{X}/{Y} = {valor:.2f}')
                    print(f'Esse é o resultado da divisão {valor:.2f}')
                    list_historico.append(operação_historico)
            else:
                #O else está aqui para caso o usuario use um operador que não seja alguma das opções oferecidas
                print('Esse é um operador invalido, por favor tente novamente!')
        print('\n')
    except ValueError:
        print('ERRO! digite um valores validos para as opções')
        #Se o codigo chega no except é devido ao usuario não ter digitado um numero em alguma das duas variaveis 