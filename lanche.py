produtos =["Cachorro quente", "X-Salada", "X-Bacon", "Torrada simples", "Refrigerante"]
precos=[4, 4.5, 5, 2, 1.5]

print("Produtos e seus códigos: \n\nCachorro quente - 1;\nX-Salada - 2;\nX-Bacon - 3;\nTorrada simples - 4;\nRefrigerante - 5;\n")

codigo = int(input("Digite o código do item da lanchonete: "))
qntdItem = int(input(f"Digite a quantidade de {produtos[codigo-1]} consumidos: "))

valor = qntdItem*precos[codigo-1]
print("Total da compra: R$%.2f"%valor)