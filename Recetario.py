import os
from pathlib import Path
from os import system

cwd = os.getcwd()
base = Path(Path.home(), "PycharmProjects", "pythonProject", "Recetas")
opcion = 0


def inicio():
    print("¡Bienvenido al recetario definitivo, chaval!")
    print("Tio, el directorio actual en el que esta alojada la carpeta de recetas es el siguiente: " + cwd)
    total_recetas = contar_recetas()
    print("El total de recetas hasta la fechas es de: " + str(total_recetas))


def volver_al_menu():
    salir = ''
    salir = input("para volver al menu, apreta cualquier caracter: ")


def contar_recetas():
    numero = 0
    for txt in Path(base).glob("**/*.txt"):
        numero += 1
    return numero


def pedir_opcion():
    opcion_elegida = ''
    es_valida = False
    opciones = str(123456)

    while not es_valida:
        opcion_elegida = input("Elige tu opcion: ")
        if opcion_elegida in opciones and len(opcion_elegida) == 1:
            es_valida = True
            return int(opcion_elegida)
        else:
            print("Seleciona bien la opcion, tio!")


def selecionar_categoria():
    numero = 0
    numero2 = 0
    categoria_elegida = ''
    for recetas in base.iterdir():
        numero += 1
        print(str(numero) + '.-' + recetas.stem)
    opcion_categoria = input("Selecciona el numero de la categoria a la que quieres acceder: ")
    for recetas in base.iterdir():
        numero2 += 1
        if str(numero2) == opcion_categoria:
            categoria_elegida = recetas
    return categoria_elegida


def opcion_1():
    numero = 0
    receta_elegida = ''
    categoria = selecionar_categoria()
    for txt in Path(categoria).glob('*.txt'):
        numero += 1
        print(str(numero) + '.-' + txt.stem)
    opcion_receta = input("Selecciona el numero de la receta a la que quieres acceder: ")
    numero = 0
    for receta in categoria.iterdir():
        numero += 1
        if str(numero) == opcion_receta:
            receta_elegida = receta
    leer_receta = open(Path(receta_elegida))
    print("La receta que has elegido es " + receta_elegida.stem + " y su contenido es el siguiente: ")
    print(leer_receta.read() + '\n')
    volver_al_menu()


while opcion < 6:
    inicio()
    print("""Chaval es hora, elige una de las siguientes opciones: 
                1.- Elige una categoria y luego elige una receta para leerla
                2.- Elige una categoria y luego crea una receta nueva
                3.- Crea una nueva caterogira
                4.- Elige una categoria, luego elige una receta para eliminarla
                5.- Elige una categoria y eliminala
                6.- Salir del recetario""")
    opcion = pedir_opcion()
    if opcion == 1:
        opcion_1()
    system('cls')
