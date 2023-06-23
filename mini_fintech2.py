# -*- coding: utf-8 -*-
"""Mini fintech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1saPlqrkVz3jUU5qDt2ZgzCCZ7a1TfWW1
"""

#valores iniciais

saldo_inicial = 1000
cod_inicial = 123

saldo = 0
extrato = ""

#faixas de investimento
limite_1 = 1500
limite_2 = 5000
limite_3 = 50000

produto_1 = "Investimentos em Tesouro direto"
produto_2 = "Fundos de Investimento"
produto_3 = "Fundos de ações"

#fluxo geral
print("Digite os valores da transação ou 's' para sair")
while True:

  if saldo == 0:
    saldo = saldo_inicial

  valor = input("Valor: ")

  if valor in "Ss":
    break

  #controle de dados
  num_pontos = valor.count(".")
  num_menos = valor.count("-")

  valor_limpo = valor.replace(".","")
  valor_limpo = valor_limpo.replace("-","")

  primeira_posicao = valor[0]

  if valor_limpo.isdigit() and num_pontos <= 1 and ((num_menos == 1 and primeira_posicao == "-") or num_menos == 0):
    valor = float(valor)
    if (saldo + valor) < 0:
      print("Saldo insuficiente: R$" + str(saldo))
    else:

      saldo = saldo + float(valor)
      #crédito
      if valor > 0:
        extrato += "\ncredito: "+ str(valor)
      else:
        extrato += "\ndebito: "+ str(valor)

      print(saldo)
  else:
    print("Seu valor está incorreto")

#Montagem do extrato
#Investimento
extrato += "\nSaldo Final: " + str(saldo)

if saldo >= limite_3:
  investimento = produto_3
elif saldo >= limite_2:
  investimento = produto_2
elif saldo >= limite_1:
  investimento = produto_1
else:
  investimento = "investimentos na Poupança"
extrato += "\n\n******* Você já conhece nossos " + investimento +"? Fale com seu gerente!*******"
print(extrato)

