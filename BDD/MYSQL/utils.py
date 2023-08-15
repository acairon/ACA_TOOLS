import mysql.connector

def connect_to_database(host, username, password, database):
    """Establece una conexión a la base de datos MySQL y devuelve el objeto de conexión."""
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    return connection

def execute_query(connection, query):
    """Ejecuta una consulta en la base de datos y devuelve los resultados."""
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results