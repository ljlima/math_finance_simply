from operacoesOrcamento import fazerBalanco


print("Bem vindo ao Software de Calculo de orçamento pessoal")
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