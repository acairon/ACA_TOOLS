import oracledb

def connect_to_database(username, password, dsn):
    """Establece una conexión a la base de datos Oracle y devuelve el objeto de conexión."""
    connection = oracledb.connect(username, password, dsn)
    return connection

def execute_query(connection, query):
    """Ejecuta una consulta en la base de datos y devuelve los resultados."""
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results