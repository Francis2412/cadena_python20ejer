def cadena_lista():
    #Recibe una lista de nombres separados por ;, crea una lista limpia y muestra cada nombre en una línea.
    lista = input("Ingresa una lista de nombre separados por ; o , ")
    listasincomas = lista.split(";")
    for nombre in listasincomas:
        nombre = nombre.strip()
        print(nombre)

def lista_cadena():
    #Crea una lista de módulos y genera una sola cadena separada por ' | '.
    lista = ["Anne", "Zack", "Brennan", "Booth"]
    cadena = "' | '".join(lista)
    print(cadena)
        

def conjunto_palabras():
    #Recibe una frase y construye un conjunto de palabras únicas en minúsculas.
    frase = input("Ingrese una frase: ")
    fraseminus = frase.lower()
    conjunto = set(fraseminus.split)
    print(conjunto)


def frecuencia_palabras():
    #Recibe una frase y construye un diccionario donde cada palabra sea una clave y su valor sea la cantidad de veces que aparece.
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    print(frecuencia)
