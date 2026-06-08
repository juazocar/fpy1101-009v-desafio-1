# Inicio del programa
print("=" * 50)
print(" HOSPITAL CENTRAL METROPOLITANO ")
print(" Sistema de Registro de Médicos ")
print("=" * 50)

# Contadores
especialistas = 0
residentes = 0

# Validar cantidad de médicos
while True:
    try:
        cantidad_medicos = int(input("¿Cuántos médicos desea registrar?: "))
        if cantidad_medicos > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

# Registro de médicos
for i in range(cantidad_medicos):
    print(f"\n--- Registro Médico {i + 1} ---")

    # Validar nombre profesional
    while True:
        nombre = input("Ingrese nombre profesional: ")

        if len(nombre) >= 6 and " " not in nombre and not nombre.isdigit():
            break
        else:
            print("Nombre inválido. Debe tener al menos 6 caracteres, no contener espacios y no estar compuesto solo por números.")

    # Validar experiencia clínica
    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia clínica: "))
            if experiencia > 0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    # Clasificación
    if experiencia > 5:
        clasificacion = "Especialista Senior"
        especialistas += 1
    else:
        clasificacion = "Residente Junior"
        residentes += 1
    
    print(f"Clasificación asignada --> {clasificacion}")

# Resumen final
print("\n===== RESUMEN FINAL =====")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior! ¡Sistema listo para operar!")