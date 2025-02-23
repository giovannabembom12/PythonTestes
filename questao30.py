# Construa um algoritmo que leia um número inteiro n e verifique se n é triangular ou não. Um numero é triangular se ele é o produto de três números inteiros consecutivos. Exemplo: 120 é triangular, pois 4 x 5 x 6 = 120. 
def verificar_numero_triangular(n):
    x = 1
    while x * (x + 1) * (x + 2) <= n:
        if x * (x + 1) * (x + 2) == n:
            return True
        x += 1
    return False

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))

if verificar_numero_triangular(numero):
    print(f"O número {numero} é triangular.")
else:
    print(f"O número {numero} não é triangular.")