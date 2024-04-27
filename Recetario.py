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


def seleccionar_categoria():
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


def seleccionar_receta(categoria):
    receta_elegida = ''
    numero = 0
    for txt in Path(categoria).glob('*.txt'):
        numero += 1
        print(str(numero) + '.-' + txt.stem)
    opcion_receta = input("Selecciona el numero de la receta a la que quieres acceder: ")
    numero = 0
    for receta in categoria.iterdir():
        numero += 1
        if str(numero) == opcion_receta:
            receta_elegida = receta
    return receta_elegida


def opcion_1():
    categoria = seleccionar_categoria()
    receta_elegida = seleccionar_receta(categoria)
    leer_receta = open(Path(receta_elegida))
    print("La receta que has elegido es " + receta_elegida.stem + " y su contenido es el siguiente: ")
    print(leer_receta.read() + '\n')
    volver_al_menu()


def opcion_2():
    categoria_elegida = seleccionar_categoria()
    nombre_receta_nueva = input("Dame el nombre de la receta nueva chaval: ") + ".txt"
    contenido_receta_nueva = input("Ahora escribe el contenido de la receta: ")
    ruta_receta_nueva = Path(categoria_elegida,nombre_receta_nueva)
    with open(Path(ruta_receta_nueva),'w') as file:
        file.write(contenido_receta_nueva)
        file.close()
    print("En hora buena primo, tu receta ha sido creada")
    volver_al_menu()


def opcion_3():
    nombre_categoria_nueva = input("Dame el nombre de la categoria que quieres crear: ")
    ruta_categoria_nueva = Path(base,nombre_categoria_nueva)
    ruta_categoria_nueva.mkdir(parents=True,exist_ok=True)
    print("En hora buena primo, tu categoria ha sido creada")
    volver_al_menu()


def opcion_4():
    categoria = seleccionar_categoria()
    receta_elegida = seleccionar_receta(categoria)
    receta_a_eliminar = Path(receta_elegida)
    receta_a_eliminar.unlink()
    print("Que pena tío, la receta se ha borrado")
    volver_al_menu()


def opcion_5():
    categoria = seleccionar_categoria()
    categoria_a_eliminar = Path(categoria)
    categoria_a_eliminar.rmdir()
    print("Que pena tío, la categoria se ha eliminado")
    volver_al_menu()


while opcion < 6:
    inicio()
    print("""Chaval es hora, elige una de las siguientes opciones: 
                1.- Elige una categoria y luego elige una receta para leerla
                2.- Elige una categoria y luego crea una receta nueva
                3.- Crea una nueva categoria
                4.- Elige una categoria, luego elige una receta para eliminarla
                5.- Elige una categoria y eliminala
                6.- Salir del recetario""")
    opcion = pedir_opcion()
    if opcion == 1:
        opcion_1()
    elif opcion == 2:
        opcion_2()
    elif opcion == 3:
        opcion_3()
    elif opcion == 4:
        opcion_4()
    elif opcion == 5:
        opcion_5()
    system('cls')
