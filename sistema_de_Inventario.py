inventario = []

while True:

    print("\n===== LABORATORIO DE ROBOTICA =====")
    print("1. Registrar componente")
    print("2. Mostrar todos los componentes")
    print("3. Filtrar por categoria")
    print("4. Actualizar stock")
    print("5. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":

        print("\n--- REGISTRAR COMPONENTE ---")

        id_componente = input("Ingrese el ID: ")


        existe = False

        for componente in inventario:
            if componente["id"] == id_componente:
                existe = True
                break

        if existe:
            print("Error: El ID ya esta registrado.")

        else:
            nombre = input("Nombre del componente: ")
            categoria = input("Categoria: ")

            stock = int(input("Cantidad disponible: "))
            precio = float(input("Precio unitario: "))


            nuevo_componente = {
                "id": id_componente,
                "nombre": nombre,
                "categoria": categoria,
                "stock": stock,
                "precio_unitario": precio
            }


            inventario.append(nuevo_componente)

            print("Componente registrado correctamente.")

    elif opcion == "2":

        print("\n--- INVENTARIO COMPLETO ---")

        if len(inventario) == 0:
            print("El inventario esta vacio.")

        else:
            for componente in inventario:

                print("\nID:", componente["id"])
                print("Nombre:", componente["nombre"])
                print("Categoria:", componente["categoria"])
                print("Stock:", componente["stock"])
                print("Precio:", componente["precio_unitario"])

    elif opcion == "3":

        print("\n--- FILTRAR COMPONENTES ---")

        categoria_buscar = input("Ingrese la categoria: ")

        encontrado = False

        for componente in inventario:

            if componente["categoria"].lower() == categoria_buscar.lower():

                print("\nID:", componente["id"])
                print("Nombre:", componente["nombre"])
                print("Stock:", componente["stock"])
                print("Precio:", componente["precio_unitario"])

                encontrado = True

        if encontrado == False:
            print("No se encontraron componentes.")

    elif opcion == "4":

        print("\n--- ACTUALIZAR STOCK ---")

        id_buscar = input("Ingrese el ID del componente: ")

        encontrado = False

        for componente in inventario:

            if componente["id"] == id_buscar:

                encontrado = True

                print("Componente:", componente["nombre"])
                print("Stock actual:", componente["stock"])

                print("\n1. Agregar unidades")
                print("2. Retirar unidades")

                movimiento = input("Seleccione una opcion: ")

                cantidad = int(input("Ingrese la cantidad: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")

                elif movimiento == "1":

                    componente["stock"] += cantidad

                    print("Stock actualizado correctamente.")
                    print("Nuevo stock:", componente["stock"])

                elif movimiento == "2":

                    if cantidad <= componente["stock"]:

                        componente["stock"] -= cantidad

                        print("Stock actualizado correctamente.")
                        print("Nuevo stock:", componente["stock"])

                    else:
                        print("Error: No hay suficiente inventario.")

                else:
                    print("Opcion no valida.")

                break

        if encontrado == False:
            print("No existe un componente con ese ID.")

    elif opcion == "5":

        print("\nGracias por utilizar el sistema.")
        break

    else:
        print("Opcion incorrecta. Intente nuevamente.")