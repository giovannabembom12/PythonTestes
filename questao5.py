#Fazer um programa que leia 20 idades de pessoas. Calcule e escreva a idade média deste grupo.
soma_idades = 0 # Inicializa a variável para armazenar a soma das idades

total_pessoas = 20 # Define o número total de pessoas

# Loop para ler as 20 idades
for i in range(1, total_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))  # Solicita a idade do usuário
    soma_idades += idade  # Adiciona a idade à soma total

# Calcula a média das idades
media_idades = soma_idades / total_pessoas

# Exibe o resultado final
print(f"A idade média do grupo é: {media_idades:.2f}")
