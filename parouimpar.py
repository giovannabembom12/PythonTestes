n = int(input("Quantas números serão inseridos?: "))  

for n in range(n):
    x = int(input("Informe o valor: "))  
    
    if x == 0:
        print("NULL")
    else:
        tipo = "EVEN" if x % 2 == 0 else "ODD" 
        sinal = "POSITIVE" if x > 0 else "NEGATIVE"  
        print(f"{tipo} e {sinal}")