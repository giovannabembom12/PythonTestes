print("Olá! Essa é uma calculadora.")
nome = input("Qual seu nome?: ")

op = input("Escolha a operação desejada (+, -, *, /, **): ")
print("⋆⭒˚.⋆🪐 ⋆⭒˚.⋆")
pn = int(input("Digite o primeiro valor: "))
sn = int(input("Digite o segundo valor: "))

if op == "+":
    print(f"O resultado é {pn+sn}.")
elif op == "-":
    print(f"O resultado é {pn-sn}.")
elif op == "*":
    print(f"O resultado é {pn*sn}.")
elif op == "/":
    if sn == 0 | pn == 0:
        print("Não foi possível realizar a operação! Verifique os valores inseridos.")
    else:
        print(f"O resultado é {pn/sn}.")
elif op == "**":
    print(f"O resultado é {pn**sn}.")
else:
    print("Operação Inválida!")
print("⋆⭒˚.⋆🪐 ⋆⭒˚.⋆")