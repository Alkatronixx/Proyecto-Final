# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-t3eoYljoUT1fQlWB0fNXKvc3psHtKfy
"""

import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print("Nombre: " + nombre + " - Anio: " + str(anio) +
          " - Duracion: " + str(duracion) + "  mins")
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)

    if (hora//100 < 10):
        hora_formato = "0" + str(hora//100)
    else:
        hora_formato = str(hora//100)

    if (hora % 100 < 10):
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict) -> None:
    out=mod.encontrar_pelicula_mas_larga(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
    mostrar_informacion_pelicula(out)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict) -> None:
    out=mod.duracion_promedio_peliculas(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
    print(out)

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, anio: int) -> None:
    out=mod.encontrar_estrenos(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,anio)
    print(out)

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict) -> None:
    out=mod.cuantas_peliculas_18_mas(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
    print(out)

def ejecutar_reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict) -> None:
    out=mod.reagendar_pelicula(peli, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    print(out)

def ejecutar_decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> None:
    out=mod.decidir_invitar(peli, edad_invitado, autorizacion_padres)
    print(out)

def iniciar_aplicacion():
    p1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    p2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")
    p3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    p4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    p5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")
    p6 = mod.crear_pelicula("Mad Max",  "ciencia-ficcion, Accion", 120, 2015, '15+', 1600, "Domingo")
    p7 = mod.crear_pelicula("Toy story",  "infantil", 81, 1995, '5+', 1200, "Miercoles")
    p8 = mod.crear_pelicula("El Padrino",  "Drama, Crimen", 175, 1972, '18+', 1900, "Domingo")
    p9 = mod.crear_pelicula("Gladiador",  "Accion, Aventura", 155, 2000, '15+', 1800, "Martes")
    p10 = mod.crear_pelicula("Jurassic Park",  "Accion, Aventura", 127, 1993, '13+', 1500, "Jueves")

    ejecutando = True
    while ejecutando:
        print("\n\nMi agenda de peliculas para la semana de receso" + "\n"+("-"*50))
        print("p1")
        mostrar_informacion_pelicula(p1)
        print("-"*50)

        print("p2")
        mostrar_informacion_pelicula(p2)
        print("-"*50)

        print("p3")
        mostrar_informacion_pelicula(p3)
        print("-"*50)

        print("p4")
        mostrar_informacion_pelicula(p4)
        print("-"*50)

        print("p5")
        mostrar_informacion_pelicula(p5)
        print("-"*50)

        print("p6")
        mostrar_informacion_pelicula(p6)
        print("-"*50)

        print("p7")
        mostrar_informacion_pelicula(p7)
        print("-"*50)

        print("p8")
        mostrar_informacion_pelicula(p8)
        print("-"*50)

        print("p9")
        mostrar_informacion_pelicula(p9)
        print("-"*50)

        print("p10")
        mostrar_informacion_pelicula(p10)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(
            p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(
            p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    elif opcion_elegida == "3":
        anio = int(input("Ingrese el año de estreno: "))
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, anio)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(
            p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    elif opcion_elegida == "5":
        print("Reagendar una pelicula de la agenda")
        nombre_pelicula = input("Ingrese el nombre de la pelicula que desea reagendar: ")
        peli = mod.encontrar_pelicula(
            nombre_pelicula, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        if peli is None:
            print("No hay ninguna pelicula con este nombre")
        nueva_hora = int(input("Ingrese la nueva hora de inicio de la pelicula: "))
        nuevo_dia = input("Ingrese el nuevo dia de inicio de la pelicula: ")
        control_horario = bool(input("Ingrese si desea controlar horario (True or False)"))
        ejecutar_reagendar_pelicula(peli,nueva_hora,nuevo_dia, control_horario, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    elif opcion_elegida == "6":
        print("Decidir si se puede invitar a alguien a ver una pelicula")
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        peli = mod.encontrar_pelicula(
            nombre_pelicula, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        if peli is None:
            print("No hay ninguna pelicula con este nombre")

        edad_invitado = int(input("Ingrese la edad del invitado: "))
        autorizacion_padres = bool(input("Ingrese si el invitado tiene autorizacion de los padres (True or False): "))

        ejecutar_decidir_invitar(peli, edad_invitado, autorizacion_padres)

    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando


iniciar_aplicacion()