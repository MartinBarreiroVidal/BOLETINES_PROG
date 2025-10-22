# Realiza un algoritmo e codifica o programa correspondente que lea, dende o teclado, unha cantidade enteira en euros e amose, por pantalla, o seu desglose en billetes de 100, 20, 5 e moedas de 1 €.

cantidade = int(input("Introduce a cantidade de euros: "))

billetes100 = cantidade // 100
resto = cantidade % 100

billetes20 = cantidade // 20
resto = cantidade % 20

billetes5 = cantidade // 5
resto = cantidade % 5

moedas1 = cantidade // 1
resto = cantidade % 1

print("Desglose:")
print("Billetes de 100: ", billetes100)
print("Billetes de 20: ", billetes20)
print("Billetes de 5: ", billetes5)
print("Moedas de 1: ", moedas1)