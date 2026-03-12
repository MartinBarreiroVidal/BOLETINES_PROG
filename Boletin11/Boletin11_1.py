"""
Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
O usuario pode engadir unha nova nota (texto libre).

As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.

O programa pode listar todas as notas gardadas.

O usuario pode buscar notas que conteñan unha palabra clave.

"""
ficheiro_notas = "notas.txt"

while True:
    print("\n1. Engadir nota")
    print("2. Ver notas")
    print("3. Buscar nota")
    print("4. Saír")

    opcion = input("Opción: ")

    if opcion == "1":
        texto = input("Escribe a nota: ")
        with open(ficheiro_notas, "a") as f:
            f.write(texto + "\n")
        print("Nota gardada.")

    elif opcion == "2":
        try:
            with open(ficheiro_notas, "r") as f:
                notas = f.readlines()
            for i, nota in enumerate(notas, 1):
                print(f"{i}. {nota.strip()}")
        except FileNotFoundError:
            print("Non hai notas gardadas.")

    elif opcion == "3":
        palabra = input("Palabra clave: ")
        try:
            with open(ficheiro_notas, "r") as f:
                notas = f.readlines()
            for nota in notas:
                if palabra.lower() in nota.lower():
                    print(nota.strip())
        except FileNotFoundError:
            print("Non hai notas gardadas.")

    elif opcion == "4":
        break