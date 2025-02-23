# Fazer um programa para achar a série de Bergamacci dos n primeiros termos: 1  1  1  1  3  5  9  17 ... 
def bergamacci(n):
    if n <= 0:
        print("Número inválido. Insira um número maior que 0.")
        return
    
    sequencia = [1, 1, 1, 1]
    for _ in range(n - 4):
        novo_termo = sequencia[-1] + sequencia[-3]
        sequencia.append(novo_termo)
    
    print("A série de Bergamacci é:", " ".join(map(str, sequencia[:n])))

n = int(input("Digite o número de termos da série de Bergamacci: "))
bergamacci(n)