# Fazer um programa que leia um conjunto de dados contendo o sexo e a altura de 50 pessoas. Escreva a altura média das mulheres.
def calcular_media_altura_mulheres():
    total_altura_mulheres = 0
    quantidade_mulheres = 0
    
    for i in range(50):
        sexo = input(f"Pessoa {i+1} - Digite o sexo (M/F): ").strip().upper()
        altura = float(input(f"Pessoa {i+1} - Digite a altura (em metros): "))
        
        if sexo == 'F':
            total_altura_mulheres += altura
            quantidade_mulheres += 1
    
    if quantidade_mulheres > 0:
        media_altura = total_altura_mulheres / quantidade_mulheres
        print(f"A altura média das mulheres é: {media_altura:.2f} metros")
    else:
        print("Nenhuma mulher foi registrada no conjunto de dados.")

# Executando a função
calcular_media_altura_mulheres()
