import sqlite3

def connect_to_database(database_name):
    """Establece una conexión a la base de datos y devuelve el objeto de conexión."""
    connection = sqlite3.connect(database_name)
    return connection

def execute_query(connection, query):
    """Ejecuta una consulta en la base de datos y devuelve los resultados."""
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results