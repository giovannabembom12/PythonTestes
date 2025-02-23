a = float(input("Informe a primeira nota: "))
b = float(input("Informe a segunda nota: "))

peso_A = 3.5
peso_B = 7.5

media = (a * peso_A + b * peso_B) / (peso_A + peso_B)

print(f"MÉDIA = {media:.5f}")