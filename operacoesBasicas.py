def somaSimples(valor1,valor2):
    return valor1+valor2

def somatorio():
    somatorio = 0.0
    valor = 0.0
    contaInsercaoValores = 0
    terminou = False
    while (terminou == False):
        valor = float(input("Insira o valor: "))
        somatorio += valor
        contaInsercaoValores += 1
        resposta = input("terminou? sim 's', não 'n' :  ")
        if(resposta == 's'):
            terminou = True

    media = somatorio/contaInsercaoValores
    return somatorio, media

def subtracao(valor1,valor2):
    return valor1-valor2

def multiplicacao(valor1,valor2):
    return valor1*valor2

def divisao(valor1,valor2):
    if(valor2 == 0):
        print("Insira um valor maior que zero!! Erro 01")
    else:
        return valor1/valor2
    
def potenciacao(valor1, expoente):
    resultado = 1
    if(expoente == 0):
        resultado = 1
    else:
        for i in range(1,expoente):
            resultado *= valor1

    return resultado
        