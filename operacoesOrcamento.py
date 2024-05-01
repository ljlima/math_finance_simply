from operacoesBasicas import soma, subtracao,multiplicacao

def passivo():
    print("\n\nInsira Despesas (gastos) e quando acabar digite 'n'\n\n")
    somatorioDespesa, despesaMedia = soma()
    
    return  somatorioDespesa, despesaMedia



def ativo():
    print("\n\nInsira receitas (ganhos) e quando acabar digite 's'\n\n")
    somatorioReceita, receitaMedia = soma()
    
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


        