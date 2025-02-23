salario = float(input("Informe o salário: ")) 

if salario <= 2000.00:
    print("Isento")
else:
    imposto = 0

    if salario > 4500.00:
        imposto += (salario - 4500.00) * 0.28
        salario = 4500.00 

    if salario > 3000.00:
        imposto += (salario - 3000.00) * 0.18
        salario = 3000.00 

    if salario > 2000.00:
        imposto += (salario - 2000.00) * 0.08

    print(f"R$ {imposto:.2f}")