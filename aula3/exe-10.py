salario = float(input("Valor Salário: "))
aumento = float(input("Porcentagem do Aumento: "))

valorAumento = salario * ( aumento / 100 )
novoSalario = salario + valorAumento

print(f"O valor do aumento é de {valorAumento:.2f}. O seu novo salário deve ser {novoSalario:.2f}.")
