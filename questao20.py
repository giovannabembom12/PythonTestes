# Construa um algoritmo que faça a conversão de um número que está na base decimal para a base binária.
def decimal_para_binario(numero):
    if numero == 0:
        return "0"  # Caso o número seja zero
    
    binario = ""
    
    while numero > 0:
        resto = numero % 2  # Obtém o resto da divisão por 2 (0 ou 1)
        binario = str(resto) + binario  # Adiciona o resto à esquerda da string binária
        numero = numero // 2  # Atualiza o número dividindo por 2
    
    return binario

# Exemplo de uso
numero = int(input("Digite um número decimal para converter para binário: "))
binario = decimal_para_binario(numero)
print(f"O número {numero} em binário é {binario}")
