from operacoesOrcamento import fazerBalanco, jurosSimplesComposto


print("$$$$$$$$$$$$$ Bem vindo ao Software de Calculo de orçamento pessoal calculo de Juros $$$$$$$$$$$$\n\n\n\n")
finalizaOperacao = 'n'

while(finalizaOperacao != 's'):

    print("Escolha a opção que deseja: \n\n")

    opcao = int(input("1. Fazer orçamento mensal\n2. Calcular Juros\n\n"))

    print(f"Opção escolhida: {opcao}")

    if(opcao == 1):
        nome = input("insira seu nome: ")
        mesBalanco = input("Insira o mes referente: ")
        anoReferente = int(input("Insira o ano referente: "))

        receitaTotal, receitaMedia, despesaTotal, despesaMedia, balanco, impostoRenda = fazerBalanco()

        print(f"\n\n\n********RESULTADO DO BALANÇO {mesBalanco} / {anoReferente} **********\n\n")
        print(f"Nome: {nome}")
        print(f"Referente ao Mês: {mesBalanco}")
        print(f"referente ao Ano: {anoReferente}")


        print("\n\n########## DADOS DO BALANÇO ###############\n\n")
        print(f"Receita Total: R$ {receitaTotal}\n")
        print(f"Despesa Total R$ {despesaTotal}\n")

        print(f"Receita Média em relação a quantas vezes ganhou no mês: R$ {receitaMedia}\n")
        print(f"Despesa Média em relação a quantas vezes gastou no mês R$ {despesaMedia}\n\n")


        if(balanco < 0):
            print(f"Seu balanço R$  {balanco} foi negativo! Precisa economizar dinheiro na próxima!\n")
        else:
            print(f"Seu balanço R$  {balanco} foi positivo! Parabéns, continue assim!\n")

        print(f"Imposto de Renda estimado: R$  {impostoRenda}\n\n\n")

        print("**********FIM!**************")

    else:
        print("\n\n***********CALCULA JUROS SIMPLES E COMPOSTO************\n\n")
        montanteJurosSimples, montanteJurosCompostos, jurosSimplesPago,jurosCompostosPago = jurosSimplesComposto()
        print(f"Valor à prazo com Juros simples: R$ {montanteJurosSimples}")
        print(f"Valor à prazo com Juros Compostos: R$ {montanteJurosCompostos}")
        print(f"Juros Simples: R$ {jurosSimplesPago}")
        print(f"Juros Compostos: R$ {jurosCompostosPago}")
    
    finalizaOperacao = input("Deseja finalizar operação? sim: 's', não 'n':   \n")