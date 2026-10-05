def registro_confi():
    #Procesa una cadena como 'host=localhost;puerto=1433;bd=ventas' y crea un diccionario con los datos.
    cadena = "host=localhost;puerto=1433;bd=venta"
    cadenadiv1 = cadena.split(";")
    cadenadiv2 = cadenadiv1.split("=")

    confi = {}

    for dato in cadenadiv1:
        clave, valor = dato.split("=")
        confi[clave] = valor

    print(confi)

def limpiezaResumen_etiquitas():
    #Recibe etiquetas separadas por comas, elimina espacios, normaliza a minúsculas,
    #elimina repetidos y produce una cadena ordenada separada por ' | '.
    etiquetas = input("Ingresa las etiquetas: ")

    etiquetaslista = etiquetas.split(",")

    etiquetaslimpias = []

    for etiqueta in etiquetaslista:
        etiqueta = etiqueta.strip().lower()
        etiquetaslimpias.append(etiqueta)

    etiquetasset = set(etiquetaslimpias)
    etiquetasordenadas = sorted(etiquetasset)

    cadena = " | ".join(etiquetasordenadas)

    print(cadena)