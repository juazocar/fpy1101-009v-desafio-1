"""
Actividad DUOC UC - Debugging con Python
Archivo de funciones: funciones.py

Este archivo contiene las funciones del CRUD.
Tiene errores intencionales de sintaxis, lógica y uso de parámetros.
"""

def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    flag = True
    flag_nombre = True
    while flag_nombre == True:
            rut = input("Ingrese RUT: ")
            if rut in [estudiante["rut"] for estudiante in estudiantes]:
                print("El rut ya se encuentra registrado.")
                print("Pruebe con otro.")
            elif rut not in [estudiante["rut"] for estudiante in estudiantes]:
                flag_nombre = False
    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")
    while flag == True:
        try:
            edad = int(input("Ingrese edad: "))
            flag = False
        except:
            print("La edad debe ser un número entero")  
    
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

    if encontrado == False:
        print("No se encontró el estudiante")


def actualizar_estudiante(estudiantes, rut):
    print("\n--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            nueva_edad = input("Ingrese nueva edad: ")

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
            flag = True
            while flag == True:
                op = input("¿Está seguro que desea eliminar este estudiante? (s/n): ")
                if op.lower() == "s":
                    estudiantes.remove(estudiante)
                    print("Estudiante eliminado correctamente")
                    flag = False
                    return
                elif op.lower() == "n":
                    print("Operación cancelada")
                    flag = False
                    return
                else:
                    print("Opción no válida")

    print("No se encontró el estudiante")
