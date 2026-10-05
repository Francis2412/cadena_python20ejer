def caracteres_cadena():
    #Solicita una cadena y muestra su primer carácter, último carácter, longitud y cadena invertida.
    cadena = input("Ingresa lo que sea: ")
    longitud = len(cadena)
    primerCaracter = cadena[0]
    ultimoCaracter = cadena[-1]
    cadenainvertida = cadena[::-1]
    print(f"Longitud: {longitud}")
    print(f"Primer caracter: {primerCaracter}")
    print(f"Ultimo caracter: {ultimoCaracter}")
    print(f"Cadena invertidad: {cadenainvertida}")

def mays_minus():
    #Solicita un texto y muestra una versión en mayúsculas, otra en minúsculas y otra con formato de título.
    cadena = input("Ingresa lo que sea: ")
    mayus = cadena.upper()
    minus = cadena.lower()
    titulo = cadena.title()
    print(f"Versión en mayúsculas: {mayus}")
    print(f"Versión en minúsculas: {minus}")
    print(f"Versión en título: {titulo}")
    

def limpieza_identificadores():
    #Transforma un identificador recibido con espacios y guiones en una versión limpia utilizando strip() y replace().
    cadena = input("Ingresa lo que sea (con espacios y guiones): ")
    espacios = cadena.strip()
    guiones = espacios.replace("-", "_")
    print(f"Version limpia: {guiones}")


def validarcorreo_basico():
    #Solicita un correo y determina si contiene @ y un punto después de este. No necesitas validar todas las reglas de un correo real.
    correo = input("Ingrese un correo: ")

    if "@" in correo:
        partes = correo.split("@")
        dominio = partes[1]
        if "." in dominio:
            print("Correo válido")
        else: 
            print("Correo inválido...")
    else:
        print("Correo inválido...")


def solo_num():
    #Solicita un código y determina si todos sus caracteres son dígitos. Si lo es, conviértelo a entero.
    codigo = input("Ingresa digitos o lo que sea: ")

    if codigo.isdigit():
        entero = int(codigo)
        print(f"Entero: {entero}")
        
    else: 
        print("No es entero")