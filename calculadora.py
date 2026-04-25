#Projeto de um sistema de calculadora para realização de operações
#A logica por trás é apenas realizar calculos das 4 operações basicas, soma, subtração, multiplicação e divisão

print('Bem vindo!')
#Essa lista existe para ser usada como historico de operações realizadas
list_historico = []
#O loop de while True serve para manter a calculadora em funcionamento e assim poder realizar varias operações seguidas
while True:
    #O comando try é um comando feito para verificar o funcionamento do codigo ao longo dele
    #Nesse caso aqui ele serve para verificar se o usuario está realmente digitando valores nas entradas das variaveis X e Y
    try:
        entrada = input("Digite a expressão a ser calculada no seguinte formato X + Y, tendo como opção as seguintes operações:\n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\nDigite:\nhist para ver o historico de operações ou exit para sair\n")
        #Após a entrada ser enviada, será feita a verificação se o usuario está pedindo para realizar uma operação, sair ou ver o historico de operações

        if entrada == 'exit':
            #Aqui é realizada o fim do funcionamento do programa à pedido do usuario
            print('Obrigado por usar nossa calculadora')
            break
        
        elif entrada == 'hist':
            #Caso o usuario tenha digitado hist logo de começo, será printado um vazio.
            #Para cada elemento na lista e seu respectivo "valor", será impresso a posição do elemento e seu "valor"
            for i, conta in enumerate(list_historico):
                print(f'{i+1}. {conta}')
                random = input()
                #Esse random input() serve para melhorar a visualização do historico de operações

        else:
            #Caso a entrada não caia em nenhuma das duas condições anteriores,
            #Aí a entrada é transformada em seus devidos valores e é relizada a operação desejada
            entrada =  entrada.split()
            X = float(entrada[0])
            operador = str(entrada[1])
            Y = float(entrada[2])

            #Aqui entramos exatamente na cadeia onde será realizada a verificação do operador
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
                    print(f'Esse é o resultado da divisão: {valor:.2f}')
                    list_historico.append(operação_historico)

            else:
                #O else está aqui para caso o usuario use um operador que não seja alguma das opções oferecidas
                print('Esse é um operador invalido, por favor tente novamente!')
        print('\n')

    except ValueError:
        print('ERRO! digite valores validos para as opções')
        #Se o codigo chega no except é devido ao usuario não ter digitado um numero em alguma das duas variaveis 