conta = float(input("Digite o valor da conta: ")) #entrada
pessoas = int(input("Quantas pessoas vão dividir? "))
gorjeta = conta * 0.1 #Processamento: 10% de gorjeta
total = conta + gorjeta
valor_por_pessoa = total / pessoas

print(f"A gorjeta é R$ {gorjeta: .2f}. Cada pessoa deve pagar R$ {valor_por_pessoa:.2f}.") #Saída