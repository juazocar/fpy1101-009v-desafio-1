def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    rut = input("Ingrese RUT: ").replace(".", "").replace("-", "").strip()
    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")
    edad = int(input("Ingrese edad: "))

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
        for estudiante in estudiantes:
            print(f"RUT: {estudiante['rut']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Edad: {estudiante['edad']}")
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


def actualizar_estudiante(estudiantes, rut):
    print("\n--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            nueva_edad = int(input("Ingrese nueva edad: "))

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
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente")
            return

    print("No se encontró el estudiante")