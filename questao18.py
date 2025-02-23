#Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas pelos seus dois primeiro e dois últimos dígitos. Exemplo: 1456 : 14 e 56. Construa um algoritmo que 
#imprima todos os números de quatro algarismos cuja raiz  quadrada seja a soma das dezenas formadas pela divisão acima. Exemplo: raiz de 9801 = 99 = 98 + 01.
import math

def verificar_raiz_soma_dezenas():
    for num in range(1000, 10000):  # Percorre todos os números de 4 algarismos
        raiz = math.isqrt(num)  # Calcula a raiz quadrada inteira (sem casas decimais)
        if raiz * raiz == num:  # Verifica se a raiz é exata
            # Separa os dois primeiros e dois últimos dígitos
            dezenas_iniciais = num // 100  # Os dois primeiros dígitos
            dezenas_finais = num % 100    # Os dois últimos dígitos
            if raiz == dezenas_iniciais + dezenas_finais:
                print(f"O número {num} é válido: raiz de {num} = {raiz} = {dezenas_iniciais} + {dezenas_finais}")

# Chama a função para imprimir os números válidos
verificar_raiz_soma_dezenas()
