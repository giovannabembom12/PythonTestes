#O número 3025 possui a seguinte característica: 
#30 + 25 = 55  
# 55^2 = 3025  
# Fazer um algoritmo que pesquise e imprima todos os números de quatro dígitos que apresentam tal característica. 
def verificar_caracteristica():
    for num in range(1000, 10000):  # Percorre todos os números de 4 algarismos
        # Separa os dois primeiros e dois últimos dígitos
        parte_inicial = num // 100  # Os dois primeiros dígitos
        parte_final = num % 100    # Os dois últimos dígitos
        
        # Soma das duas partes
        soma = parte_inicial + parte_final
        
        # Verifica se o quadrado da soma é igual ao número original
        if soma ** 2 == num:
            print(f"O número {num} possui a característica: {parte_inicial} + {parte_final} = {soma} e {soma}^2 = {num}")

# Chama a função para imprimir os números válidos
verificar_caracteristica()
