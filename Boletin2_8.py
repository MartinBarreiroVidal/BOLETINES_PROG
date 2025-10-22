# Deseña un programa para o software dunha máquina, que converta unha cantidade enteira de diñeiro, que está presentada en billetes de 100, 20, 5 e moedas de 1 €, no seu equivalente en euros. Por exemplo 2 billetes de 100€, 	3 billetes de 20 €, 6 moedas de 1€ visualizaríamos 266 €.

billete100 = int(input("Ingrese o número de billetes de 100: "))
billete20 = int(input("Ingrese o número de billetes de 20: "))
billete5 = int(input("Ingrese o número de billetes de 5: "))
moedas1 = int(input("Ingrese o número de moedas de 1: "))

total= billete100 * 100 + billete20 * 20 + billete5 * 5 + moedas1

print("El total de diñeiro é: ", total, "€")