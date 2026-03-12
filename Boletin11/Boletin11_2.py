"""
Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
Solicita ao usuario o nome dun ficheiro .txt.

Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).

Gárdase un resumo nun novo ficheiro resumo_palabras.txt.

Este texto ten que ser onde vou a buscar as palabras. Para iso teño que percorrer unha lista de palabras e contalas.
Por liña:
    Eliminar caracteres especias ! ¿ ? ' " , . ; :
    Separo palabras
    Bucar palabra no diccionario:
                                si entra sumo 1 cantidade
                                Non esta engado o diccionario
"""
import string

nome = input (" Ingrese o nome do ficheiro .txt: ")

try:
    with open(nome, "r") as f:
        linhas = f.readlines()

    frecuencias = {}

    for linha in linhas:
        linha = linha.lower()

        for signo in "\!¿?'\",.:;/¡":
            linha  = linha.replace(signo, "")

        palabras = linha.split()
        for palabra in palabras:
            if palabra in frecuencias: # Si la palabra se encuentra en el diccionario,
                frecuencias[palabra] += 1 # Sumamos 1
            else:
                frecuencias[palabra] = 1 # Si no está, la añadimos al diccionario

    print("\nFrecuencia de palabras:")
    for palabra in frecuencias:
        print(f"{palabra}: {frecuencias[palabra]}")

    with open("resumo_palabras.txt", "w") as f:
        for palabra in frecuencias:
            f.write(f"{palabra}: {frecuencias[palabra]}")

    print("Resumo gardado en resumo_palabras.txt")
except FileNotFoundError:
    print("O ficheiro non existe")








