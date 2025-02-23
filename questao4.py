#Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor. 
v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um valor maior que o anterior: "))

if v1>=v2:
    print("O segundo valor deve ser maior que o primeiro!")
    v2 = int(input("Digite um valor maior que o primeiro: "))
else:
    print("Tudo certo, camarada!")