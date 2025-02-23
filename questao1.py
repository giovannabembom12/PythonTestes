#Exibir a soma dos números positivos no intervalo de um a cem. 
i = 1 #inicializa o contador
soma = 0 #inicializa a variavél de cálculo
while i <= 100: #enquanto o contador for menor ou igual a 100
    soma += i #a soma recebe o próprio valor da soma + o valor do contador
    i +=1 #adiciona-se um ao contador
print(f"Soma: {soma}") #imprimi o valor final