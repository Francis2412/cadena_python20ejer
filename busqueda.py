def buscar_palabra():
    #Solicita una frase y una palabra. Indica si la palabra aparece y en qué posición comienza.
    frase = input("Ingresa un frase: ")
    palabra = input("Ingresa una palabra (puede ser de la frase): ")
    posicion = frase.find(palabra)
    
    if posicion != -1:
        print(f"La palabra esta en la posicion: {posicion}")
    
    else: print("La palabra no aparece en la frase...")

def contar_caract():
    #Solicita una cadena y un carácter. Indica cuántas veces aparece el carácter sin distinguir mayúsculas de minúsculas.
    cadena = input("Ingresa cualquier cosa: ")
    caract = input("Ingresa el carácter que deseas contar: ")
    
    filtro = cadena.lower().count(caract.lower())
    print(f"El caracter '{caract}' aparece {filtro} veces")

def prefijo_extencion():
    #Solicita el nombre de un archivo e indica si termina en .csv y si comienza con reporte.
    nombre = input("ingresa un nombre de un archivo: ")

    if nombre.startswith("reporte") and nombre.endswith(".csv"):
        print("El archhivo cumple con las condiciones.")

    else:
        print("El archivo no cumple con las condiciones...")
    

def palindromo():
    #Determina si una palabra es un palíndromo ignorando mayúsculas y espacios.
    palabra = input("Ingresa una palabra: ")
    palabrasinespacio = palabra.replace(" ", "")
    palabraenminus = palabrasinespacio.lower()
    palabravolteada = palabraenminus[::-1]

    if palabravolteada == palabraenminus:
        print("La palabras es un palíndromo")
    else:
        print("La palabras no es un palíndromo")