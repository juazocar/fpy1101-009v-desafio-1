# Variables iniciales
stock_libros = 120
prestamos_activos = 0
historial_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:

    print("\n===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Opción 1
    if opcion == "1":
        print(f"Libros disponibles: {stock_libros}")

    # Opción 2
    elif opcion == "2":

        while True:
            try:
                cantidad = int(input("Cantidad de libros a prestar: "))

                if cantidad <= 0:
                    print("Debe ingresar una cantidad mayor a 0.")

                elif cantidad > stock_libros:
                    print("No hay suficientes libros disponibles.")

                else:
                    stock_libros -= cantidad
                    prestamos_activos += cantidad
                    historial_prestamos += 1

                    print("Préstamo realizado correctamente.")
                    break

            except ValueError:
                print("Ingrese un número válido.")

    # Opción 3
    elif opcion == "3":

        if prestamos_activos == 0:
            print("No existen préstamos vigentes para devolver.")

        else:
            while True:
                try:
                    cantidad = int(input("Cantidad de libros a devolver (0 para cancelar): "))

                    if cantidad <= 0:
                        print("Debe ingrsar una cantidad mayor a 0.")

                    elif cantidad > prestamos_activos:
                        print("No puede devolver más libros de los actualmente prestados.")

                    else:
                        stock_libros += cantidad
                        prestamos_activos -= cantidad

                        print("Devolución realizada correctamente.")
                        break

                except ValueError:
                    print("Ingrese un número válido.")

    # Opción 4
    elif opcion == "4":

        print(f"Préstamos activos: {prestamos_activos}")
        print(f"Total de préstamos realizados en la sesión: {historial_prestamos}")

    # Opción 5
    elif opcion == "5":

        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    # Opción inválida
    else:
        print("Opción no válida.")