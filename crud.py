import mysql.connector
import pandas as pd
import configparser

def establish_connection():
    config = configparser.ConfigParser()
    config.read('.env')

    host = config.get('mysql', 'host')
    user = config.get('mysql', 'user')
    password = config.get('mysql', 'password')
    database = config.get('mysql', 'database')

    db_params = {
        "host": host,
        "user": user,
        "password": password,
        "database": database
    }

    conn = mysql.connector.connect(**db_params)
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn, cursor):
    cursor.close()
    conn.close()

def list_records():
    conn, cursor = establish_connection()
    cursor.execute("SELECT * FROM task_personal")
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=column_names)
    close_connection(conn, cursor)
    return df

def print_table(dataframe):
    print(dataframe.to_markdown(index=False))

def list_records_id(task_id):
    conn, cursor = establish_connection()
    sql = "SELECT * FROM task_personal WHERE id = %s"
    cursor.execute(sql, (task_id,))
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=column_names)
    close_connection(conn, cursor)
    return df

def print_table_id(dataframe):
    print(dataframe.to_markdown(index=False))

def save_records(description, responsible, status, priority, start_date, end_date, close_date, tags):
    conn, cursor = establish_connection()
    sql = "INSERT INTO task_personal (description, responsible, status, priority, start_date, end_date, close_date, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (description, responsible, status, priority, start_date, end_date, close_date, tags)
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registro guardado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al guardar el registro: {err}")
    finally:
        close_connection(conn, cursor)

def edit_records(task_id, description, responsible, status, priority, start_date, end_date, close_date, tags):
    conn, cursor = establish_connection()
    sql = "UPDATE task_personal SET description = %s, responsible = %s, status = %s, priority = %s, start_date = %s, end_date = %s, close_date = %s, tags = %s WHERE id = %s"
    values = (description, responsible, status, priority, start_date, end_date, close_date, tags, task_id)
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registro editado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al editar el registro: {err}")
    finally:
        close_connection(conn, cursor)

def delete_records(task_id):
    conn, cursor = establish_connection()
    sql = "DELETE FROM task_personal WHERE id = %s"
    try:
        cursor.execute(sql, (task_id,))
        conn.commit()
        print(f"Registro con ID {task_id} eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el registro: {err}")
    finally:
        close_connection(conn, cursor)
