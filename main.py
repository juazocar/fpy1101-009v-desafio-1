"""
Actividad DUOC UC - Debugging con Python
Archivo principal: main.py

IMPORTANTE:
Este programa contiene errores intencionales.
La misión del estudiante es clonar el repositorio, crear una rama,
corregir los errores y dejar funcionando el CRUD.
"""

from funciones import (
    agregar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)

estudiantes = [
    {
        "rut": "12345678-9",
        "nombre": "Juan Pérez",
        "carrera": "Ingeniería en Informática",
        "edad": 20
    },
    {
        "rut": "98765432-1",
        "nombre": "María García",
        "carrera": "Analista Programador",
        "edad": 22
    }   
]

def mostrar_menu():
    print("\n===== SISTEMA CRUD ESTUDIANTES DUOC UC =====")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")

opcion = 0

while opcion != 6:
    mostrar_menu()

    try:
        opcion = input("Seleccione una opción: ")
        
    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if opcion == "1":
        agregar_estudiante(estudiantes)

    elif opcion == "2":
        listar_estudiantes(estudiantes)

    elif opcion == "3":
        rut = input("Ingrese RUT del estudiante a buscar: ")
        buscar_estudiante(estudiantes, rut)

    elif opcion == "4":
        rut = input("Ingrese RUT del estudiante a actualizar: ")
        actualizar_estudiante(estudiantes, rut)

    elif opcion == "5":
        rut = input("Ingrese RUT del estudiante a eliminar: ")
        eliminar_estudiante(estudiantes, rut)

    elif opcion == "6":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida")
