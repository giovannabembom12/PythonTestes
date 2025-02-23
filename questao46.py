#A conversão de graus Farenheit para centígrados é obtida pela fórmula C = (5/9)*(F – 32). Escreva um programa que calcule e escreva uma tabela de graus centígrados em função de graus Farenheit que variam de 50 a 150 de 1 em 1. 
print("Fahrenheit | Celsius")
print("--------------------")

for f in range(50, 151):
    c = (5/9) * (f - 32)
    print(f"{f:10} | {c:.2f}")