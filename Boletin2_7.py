# Realiza o ordinograma e despois codifica un programa que reciba como dato de entrada o valor dunha temperatura expresada en graos centígrados e calcule o seu equivalente en graos Fahrenheit e graos Kelvin.

temperaturaCentigrados = int(input("Ingrese el temperatura en Graos Centigrados: "))
temperaturaFahrenheit = (temperaturaCentigrados * 9/5) + 32
temperaturaKelvin = temperaturaCentigrados + 273,15

print("La temperatura en Grados Fahrenheit es: ", temperaturaFahrenheit)
print("La temperatura en Grados Kelvin es: ", temperaturaKelvin)