#Modulo responsavel pelas operações matematicas da calculadora e seu historico

list_historico = []

def soma(X,Y):
    valor = X+Y
    operacao_historico = str(f'{X} + {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def subtracao(X,Y):
    valor = X-Y
    operacao_historico = str(f'{X} - {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def multiplicacao(X,Y):
    valor = X*Y
    operacao_historico = str(f'{X} x {Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def divisao(X,Y):
    #Essa cadeia de condicional alinhada serve para caso onde o usuario tente fazer divisão por 0 e o codigo não falhe
    if X == 0  and Y == 0:
        operacao_historico = str('0/0 = Indeterminação')
        list_historico.append(operacao_historico)
        return operacao_historico

    elif Y == 0:
        operacao_historico = str(f'{X}/0 = Indefinido')
        list_historico.append(operacao_historico)
        return operacao_historico
    else:
        valor = X/Y
        operacao_historico = str(f'{X}/{Y} = {valor:.2f}')
        list_historico.append(operacao_historico)
        return operacao_historico
    
def potencia(X,Y):
    valor = X**Y
    operacao_historico = str(f'{X}^{Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico

def raiz(X,Y):
    valor = Y**(1/X)
    operacao_historico = str(f'{round(X)}\/{Y} = {valor:.2f}')
    list_historico.append(operacao_historico)
    return operacao_historico