"""
Actividad DUOC UC - Debugging con Python
Archivo de funciones: funciones.py

Este archivo contiene las funciones del CRUD.
Tiene errores intencionales de sintaxis, lógica y uso de parámetros.
"""

def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    rut = input("Ingrese RUT: ")
    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            print("Error: ya existe un estudiante con ese RUT.")
            return
    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            break
        except ValueError:
            print ("Debe ingresar un numero")

    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente")


def listar_estudiantes(estudiantes):
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for i in range(len(estudiantes)):
            print(f"RUT: {estudiantes[i]['rut']}")
            print(f"Nombre: {estudiantes[i]['nombre']}")
            print(f"Carrera: {estudiantes[i]['carrera']}")
            print(f"Edad: {estudiantes[i]['edad']}")
            print("------------------------")


def buscar_estudiante(estudiantes, rut):
    print("\n--- Buscar estudiante ---")

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            print("Estudiante encontrado")
            print(f"RUT: {estudiante['rut']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Edad: {estudiante['edad']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el estudiante")

def actualizar_estudiante(rut, estudiantes ):
    print("\n--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            while True:
                try:         
                    nueva_edad = int(input("Ingrese nueva edad: "))
                    break
                except ValueError:
                    print ("Debe ingresar un numero")

            estudiante["nombre"] = nuevo_nombre
            estudiante["carrera"] = nueva_carrera
            estudiante["edad"] = nueva_edad

            print("Estudiante actualizado correctamente")
            return

    print("No se encontró el estudiante")


def eliminar_estudiante(estudiantes, rut):
    print("\n--- Eliminar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            confirmar = input(f"¿Está seguro de eliminar a {estudiante['nombre']}? (S/N): ")
            if confirmar.upper() == "S":
                estudiantes.remove(estudiante)
                print("Estudiante eliminado correctamente")
            else:
                print("Eliminacion cancelada")
            return

    print("No se encontró el estudiante")