def normalizar_unNombre():
    #Recibe un nombre con espacios innecesarios y mezcla de mayúsculas/minúsculas.
    #Limpia los extremos y presenta el nombre en formato título.
    nombre = "  aNa mArTiNeZ  "
    nombre = nombre.strip().title()
    print(nombre)


def separar_tecnologias():
    #Convierte una cadena de tecnologías separadas por comas en una lista limpia, eliminando los espacios alrededor de cada elemento.
    texto = "Python, SQL, Git, Docker"
    tecnologias = [item.strip() for item in texto.split(",")]
    print(tecnologias)

def eliminarTenologias_repetidas():
    #A partir de una cadena con tecnologías repetidas, construye un conjunto que conserve únicamente los valores únicos.
    texto = "Python,SQL,Python,Git,SQL"
    tecnologias = {item.strip() for item in texto.split(",")}
    print(tecnologias)

def construir_diccionario():
    #Procesa una cadena con pares clave=valor separados por punto y coma y construye un diccionario.
     
    texto = "cpu=Intel;ram=16;ssd=512"
    datos = {}
    for parte in texto.split(";"):
        clave, valor = parte.split("=")
        datos[clave] = valor
    print(datos)
    

def contar_palabras():
    #Recibe una frase y determina cuántas palabras contiene después de eliminar espacios innecesarios.
    frase = "  Python permite procesar texto  "
    palabras = frase.strip().split()
    print("Cantidad:", len(palabras))