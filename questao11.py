# Fazer um algoritmo para achar o fatorial de um número N. 
def calcular_fatorial():
    n = int(input("Digite um número inteiro: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é: {fatorial}")

# Executando a função
calcular_fatorial()