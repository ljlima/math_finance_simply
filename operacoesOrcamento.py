from operacoesBasicas import somatorio, subtracao,multiplicacao, potenciacao, divisao,somaSimples

def passivo():
    print("\n\nInsira Despesas (gastos) e quando acabar digite 'n'\n\n")
    somatorioDespesa, despesaMedia = somatorio()
    
    return  somatorioDespesa, despesaMedia



def ativo():
    print("\n\nInsira receitas (ganhos) e quando acabar digite 's'\n\n")
    somatorioReceita, receitaMedia = somatorio()
    
    return somatorioReceita, receitaMedia


def fazerBalanco():
    receitaTotal, receitaMedia = ativo()
    despesaTotal, despesaMedia = passivo()

    balanco = subtracao(receitaTotal,despesaTotal)
    
    if(balanco > 2553.32 ):
        impostoRenda = multiplicacao(balanco,0.27)
    else:
        impostoRenda = 0.00
    

    return receitaTotal, receitaMedia, despesaTotal, despesaMedia, balanco, impostoRenda


        
def jurosSimplesComposto():
    valorInical = float(input("Insira o valor da compra à vista: "))
    juros = float(input("Insira o juros simples em porcentagem:  "))/100
    numeroMeses = int(input("Insira a quantidade de parcelas:  "))

    jurosSimplesPago = multiplicacao(valorInical,numeroMeses)
    jurosSimplesPago = multiplicacao(jurosSimplesPago,juros)
    valorTotalJurosSimples = somaSimples(valorInical,jurosSimplesPago)

    potenciaJuros = potenciacao(1+juros,numeroMeses)
    valorTotalJurosCompostos = multiplicacao(valorInical,potenciaJuros)
    jurosCompostosPago = subtracao(valorTotalJurosCompostos,valorInical)

    return valorTotalJurosSimples, valorTotalJurosCompostos, jurosSimplesPago, jurosCompostosPago



