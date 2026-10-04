import os 
from resueltos import normalizar_unNombre, separar_tecnologias, eliminarTenologias_repetidas, construir_diccionario, contar_palabras
from basicas import caracteres_cadena, mays_minus, limpieza_identificadores, validarcorreo_basico, solo_num
from busqueda import buscar_palabra, contar_caract, prefijo_extencion, palindromo 
from estructuras import cadena_lista, lista_cadena, conjunto_palabras, frecuencia_palabras
from integracion import registro_confi, limpiezaResumen_etiquitas

def main():
    os.system("cls")
    print("*********** MENU DE LOS EJERCICOS ***********")
    print("                                             ")
    print("**************** Resueltos  *****************")
    print("1........................Normalizar un nombre")
    print("2.........................Separar tecnologías")
    print("3..............Eliminar tecnologías repetidas")
    print("4....................Construir un diccionario")
    print("5.............................Contar palabras")
    print("                                             ")
    print("**************** Básicas ********************")
    print("6....................Caracteres de una cadena")
    print("7.....................Mayúsculas y minúsculas")
    print("8.................Limpieza de identificadores")
    print("9.......................Validar correo básico")
    print("10...............................Solo números")
    print("                                             ")
    print("****************** Búsqueda *****************")     
    print("11.........................Buscar una palabra")
    print("12..........................Contar caracteres")
    print("13........................Prefijo y extensión")
    print("14.................................Palíndromo")
    print("                                             ")
    print("************** Estructuras ******************")
    print("15.............................Cadena a lista")
    print("16.............................Lista a cadena")
    print("17.......................Conjunto de palabras")
    print("18.....................Frecuencia de palabras") 
    print("                                             ")
    print("**************** Recursos *******************")
    print("19..................Registro de configuración")
    print("20............Limpieza y resumen de etiquetas")

    opc = int(input("Ingrese el número del ejercicio que desea ejecutar: "))
    match opc:
        case 1:
            normalizar_unNombre()
        case 2: 
            separar_tecnologias()
        case 3: 
            eliminarTenologias_repetidas()
        case 4:
            construir_diccionario()
        case 5: 
            contar_palabras()
        case 6: 
            caracteres_cadena()
        case 7:
            mays_minus()
        case 8:
            limpieza_identificadores()
        case 9:
            validarcorreo_basico()
        case 10:
            solo_num()
        case 11:
            buscar_palabra()
        case 12:
            contar_caract()
        case 13:
            prefijo_extencion()
        case 14:
            palindromo()
        case 15:
            cadena_lista()
        case 16:
            lista_cadena()
        case 17:
            conjunto_palabras()
        case 18:
            frecuencia_palabras()
        case 19:
            registro_confi()
        case 20:
            limpiezaResumen_etiquitas()
    
main()
    