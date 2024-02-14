from crud import *

def menu_principal():
    while True:
        print("\n\n")
        print("1. Listar registros")
        print("2. Guardar nuevo registro")
        print("3. Editar registro")
        print("4. Eliminar registro")
        print("5. Salir")
        print("\n\n")

        option = input("Selecciona una opción (1-5): ")
        print("\n\n")

        if option == "1":
            df = list_records()
            print_table(df)
            print("\n\n")

        elif option == "2":
            description = input("Ingrese la descripción de esta tarea: ")
            responsible = input("Ingrese el responsable de la tarea: ")
            while True:
                try:
                    print("Los siguientes son los estados de la tarea: ")
                    print("1. To Do")
                    print("2. In progress")
                    print("3. Done")
                    status = int(input("Selecciona el estado de la tarea (1-3): "))

                    if status in [1, 2, 3]:
                        break
                    elif not status:
                        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
                    else:
                        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
                except ValueError:
                    print("Los siguientes son los estados de la tarea: ")
                    print("1. To Do")
                    print("2. In progress")
                    print("3. Done")
                    print("Por favor, selecciona 1, 2 o 3.")
            while True:
                try:
                    print("Los siguientes son las prioridades de la tarea: ")
                    print("1. Low")
                    print("2. Mid")
                    print("3. High")
                    priority = int(input("Ingrese la prioridad de la tarea: "))

                    if priority in [1, 2, 3]:
                        break
                    elif not priority:
                        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
                    else:
                        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
                except ValueError:
                    print("Los siguientes son las prioridades de la tarea: ")
                    print("1. Low")
                    print("2. Mid")
                    print("3. High")
            start_date = input("Ingrese la fecha de creación de la tarea (AAAA-MM-DD): ")
            end_date = input("Ingrese la fecha de cierre de la tarea (AAAA-MM-DD): ")
            tags = input("Ingrese las etiquetas de la tarea: ")

            save_records(description, responsible, status, priority, start_date, end_date, None, tags)
            print("\n\n")

        elif option == "3":
            df = list_records()
            print_table(df)
            print("\n\n")

            task_id = int(input("Selecciona el ID del registro a editar: "))
            print("\n\n")

            df = list_records_id(task_id)
            print_table_id(df)

            task_id = df.loc[0, 'id']
            creation_date = df.loc[0, 'creation_date']
            description = df.loc[0, 'description']
            responsible = df.loc[0, 'responsible']
            status = df.loc[0, 'status']
            priority = df.loc[0, 'priority']
            start_date = df.loc[0, 'start_date']
            end_date = df.loc[0, 'end_date']
            close_date = df.loc[0, 'close_date']
            tags = df.loc[0, 'tags']

            aux_description = input("Ingrese la descripción de esta tarea: ")
            if aux_description != "":
                description = aux_description

            aux_responsible = input("Ingrese el responsable de la tarea: ")
            if aux_responsible != "":
                responsible = aux_responsible

            print("Los siguientes son los estados de la tarea: ")
            print("1. To Do")
            print("2. In progress")
            print("3. Done")
            aux_status = input("Selecciona una opción (1-3): ")
            if aux_status != "":
                status = aux_status

            print("Los siguientes son las prioridades de la tarea: ")
            print("1. Low")
            print("2. Mid")
            print("3. High")
            aux_priority = input("Selecciona una opción (1-3): ")
            if aux_priority != "":
                priority = aux_priority

            aux_start_date = input("Ingrese la fecha de creación de la tarea (AAAA-MM-DD): ")
            if aux_start_date != "":
                start_date = aux_start_date

            aux_end_date = input("Ingrese la fecha de cierre de la tarea (AAAA-MM-DD): ")
            if aux_end_date != "":
                end_date = aux_end_date

            aux_close_date = input("Ingrese la fecha de cumplimiento de la tarea (AAAA-MM-DD): ")
            if aux_close_date != "":
                close_date = aux_close_date

            aux_tags = input("Ingrese las etiquetas: ")
            if aux_tags != "":
                tags = aux_tags

            edit_records(int(task_id), description, responsible, int(status), int(priority), start_date, end_date, close_date, tags)
            print("\n\n")

        elif option == "4":
            df = list_records()
            print_table(df)
            print("\n\n")

            task_id = int(input("Selecciona el ID del registro a eliminar: "))
            print("\n\n")

            delete_records(task_id)
            print(f"Registro con ID #{task_id} fue eliminado exitosamente!")
            print("\n\n")

        elif option == "5":
            print("Saliendo del programa.")
            print("\n\n")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
            print("\n\n")
