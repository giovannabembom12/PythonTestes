# Fazer um programa para achar a série de Fibonacci dos n primeiros termos: 1  1  2  3  5  8  13 ...
def fibonacci(n):
    a, b = 1, 1
    sequencia = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        sequencia.append(b)
    print("A série de Fibonacci é:", " ".join(map(str, sequencia)))

n = int(input("Digite o número de termos da série de Fibonacci: "))
fibonacci(n)
