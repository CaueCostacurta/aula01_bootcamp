constante_bonus = 1000

print("Calculo de KPIs")

nome = input("Digite um nome: ")
salario = float(input("Digite o salario: "))
perc_bonus = float(input("Digite a porcentagem do bonus: "))
valorDoBonus = constante_bonus + (salario * perc_bonus)

print(f"{nome}, o valor do seu bonus salarial eh: {valorDoBonus}")