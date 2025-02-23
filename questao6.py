#Fazer um programa que leia um conjunto de idades de pessoas. O final do conjunto de valores é conhecido através do valor -1. Calcule e escreva a idade média deste conjunto. 
soma_idades = 0
np = 0

while True: # loop infinito e controla a saída com break quando -1 for digitado.
    idade = int(input("Escreva a idade da pessoa (-1 para sair): "))
    
    if idade == -1:  # Se o usuário digitar -1, interrompe o loop
        break
    
    soma_idades += idade  # Adiciona a idade à soma total
    np += 1  # Conta o número de pessoas

# Verifica se pelo menos uma idade foi inserida antes de calcular a média
if np > 0:
    total = soma_idades / np
    print(f"A idade média do grupo é: {total:.2f}") # .2f - duas casas após a virgula
else:
    print("Nenhuma idade foi informada.")
