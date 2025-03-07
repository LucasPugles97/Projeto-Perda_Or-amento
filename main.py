orçamento = float(input("Digite o valor do orçamento da campanha: "))

porcentagem_de_perda = float(input("Digite o valor em porcentagem com ponto(exemplo 25% = 0.25) de perda por orçamento: "))

calculo = orçamento / (1-porcentagem_de_perda)

print(calculo)