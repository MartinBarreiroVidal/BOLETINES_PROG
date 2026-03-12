# 11 Escribir funcións que dada unha cadena de caracteres:
# Imprima os dous primeiros caracteres.
#
# Imprima os tres últimos caracteres.
#
# Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca
# Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.

palabra = input("Dime una palabra: ")
print(palabra[0 : 2])

numero = len(palabra)
posicion = numero - 3
print(palabra[posicion:numero])

print(palabra [0:numero:2])


print(palabra,palabra[::-1])