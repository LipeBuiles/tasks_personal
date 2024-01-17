import mysql.connector
import pandas as pd

# Configuración de la conexión
db_params = {
    "host": "",
    "user": "",
    "password": "",
    "database": ""
}

# Función para establecer la conexión y el cursor
def establecer_conexion():
    conn = mysql.connector.connect(**db_params)
    cursor = conn.cursor()
    return conn, cursor

# Función para cerrar la conexión y el cursor
def cerrar_conexion(conn, cursor):
    cursor.close()
    conn.close()

# Función para listar todos los registros en la tabla
def listar_registros():
    conn, cursor = establecer_conexion()
    cursor.execute("SELECT * FROM task_personal")
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=column_names)
    cerrar_conexion(conn, cursor)
    return df

# Función para imprimir un DataFrame en formato Markdown
def imprimir_tabla(dataframe):
    print(dataframe.to_markdown(index=False))

# Función para listar registro en la tabla por ID
def listar_registros_id(task_id):
    conn, cursor = establecer_conexion()
    sql = "SELECT * FROM task_personal WHERE id = %s"
    cursor.execute(sql, (task_id,))
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=column_names)
    cerrar_conexion(conn, cursor)
    return df

# Función para imprimir un DataFrame en formato Markdown por ID
def imprimir_tabla_id(dataframe):
    print(dataframe.to_markdown(index=False))

# Función para guardar un nuevo registro
def guardar_registro(description, responsible, status, priority, start_day, end_date, close_date, tags):
    conn, cursor = establecer_conexion()
    sql = "INSERT INTO task_personal (description, responsible, status, priority, start_day, end_date, close_date, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (description, responsible, status, priority, start_day, end_date, close_date, tags)
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registro guardado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al guardar el registro: {err}")
    finally:
        cerrar_conexion(conn, cursor)

# Función para editar un registro existente
def editar_registro(task_id, description, responsible, status, priority, start_day, end_date, close_date, tags):
    conn, cursor = establecer_conexion()
    sql = "UPDATE task_personal SET description = %s, responsible = %s, status = %s, priority = %s, start_day = %s, end_date = %s, close_date = %s, tags = %s WHERE id = %s"
    values = (description, responsible, status, priority, start_day, end_date, close_date, tags, task_id)
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registro editado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al editar el registro: {err}")
    finally:
        cerrar_conexion(conn, cursor)

# Función para eliminar un registro por ID
def eliminar_registro(task_id):
    conn, cursor = establecer_conexion()
    sql = "DELETE FROM task_personal WHERE id = %s"
    try:
        cursor.execute(sql, (task_id,))
        conn.commit()
        print(f"Registro con ID #{task_id} fue eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el registro: {err}")
    finally:
        cerrar_conexion(conn, cursor)

# Menú
while True:
    print("1. Listar registros")
    print("2. Guardar nuevo registro")
    print("3. Editar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    print("\n\n")

    opcion = input("Selecciona una opción (1-5): ")
    print("\n\n")

    if opcion == "1":
        df = listar_registros()
        imprimir_tabla(df)
        print("\n\n")

    elif opcion == "2":
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
                    break  # Sale del bucle si la opción es válida
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
        priority = input("Ingrese la prioridad de la tarea: ")
        while True:
            try:
                print("Los siguientes son las prioridades de la tarea: ")
                print("1. Low")
                print("2. Mid")
                print("3. High")
                status = int(input("Selecciona el estado de la tarea (1-3): "))
                if status in [1, 2, 3]:
                    break  # Sale del bucle si la opción es válida
                else:
                    print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
            except ValueError:
                print("Los siguientes son las prioridades de la tarea: ")
                print("1. Low")
                print("2. Mid")
                print("3. High")
        start_day = input("Ingrese la fecha de creación de la tarea (AAAA-MM-DD): ")
        end_date = input("Ingrese la fecha de cierre de la tarea (AAAA-MM-DD): ")
        tags = input("Ingrese las etiquetas de la tarea: ")

        guardar_registro(description, responsible, status, priority, start_day, end_date, None, tags)
        print("\n\n")

    elif opcion == "3":
        df = listar_registros()
        imprimir_tabla(df)
        print("\n\n")

        task_id = int(input("Selecciona el ID del registro a editar: "))
        print("\n\n")

        df = listar_registros_id(task_id)
        imprimir_tabla_id(df)

        task_id = df.loc[0, 'id']
        creation_date = df.loc[0, 'creation_date']
        description = df.loc[0, 'description']
        responsible = df.loc[0, 'responsible']
        status = df.loc[0, 'status']
        priority = df.loc[0, 'priority']
        start_day = df.loc[0, 'start_day']
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

        aux_start_day = input("Ingrese la fecha de creación de la tarea (AAAA-MM-DD): ")
        if aux_start_day != "":
            start_day = aux_start_day

        aux_end_date = input("Ingrese la fecha de cierre de la tarea (AAAA-MM-DD): ")
        if aux_end_date != "":
            end_date = aux_end_date

        aux_close_date = input("Ingrese la fecha de cumplimiento de la tarea (AAAA-MM-DD): ")
        if aux_close_date != "":
            close_date = aux_close_date

        aux_tags = input("Ingrese las etiquetas: ")
        if aux_tags != "":
            tags = aux_tags

        editar_registro(int(task_id), description, responsible, int(status), int(priority), start_day, end_date, close_date, tags)
        print("\n\n")

    elif opcion == "4":
        df = listar_registros()
        imprimir_tabla(df)
        print("\n\n")

        task_id = int(input("Selecciona el ID del registro a eliminar: "))
        print("\n\n")

        eliminar_registro(task_id)
        print(f"Registro con ID #{task_id} fue eliminado exitosamente!")
        print("\n\n")

    elif opcion == "5":
        print("Saliendo del programa.")
        print("\n\n")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
        print("\n\n")