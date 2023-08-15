import os
import unittest

from BDD.MYSQL import utils as connect_to_mysql
from BDD.ORACLE import utils as connect_to_oracledb
from BDD.SQLITE import utils as connect_to_sqlite

from dotenv import load_dotenv

load_dotenv()

class TestConnections(unittest.TestCase):
    def test_sqlite_connection(self):
        conn = connect_to_sqlite(os.environ.get("DATABASE_NAME"))
        self.assertIsNotNone(conn)
        conn.close()

    def test_mysql_connection(self):
        conn = connect_to_mysql(os.environ.get('HOST'), os.environ.get('DATABASE'), os.environ.get('USER'), os.environ.get('PASSWORD'))
        self.assertIsNotNone(conn)
        conn.close()

    def test_oracledb_connection(self):
        conn = connect_to_oracledb(os.environ.get('USER'), os.environ.get('PASSWORD'), os.environ.get('DNS'))
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    connection_type = input("Selecciona la conexión que deseas probar (sqlite / mysql / oracledb): ").lower()

    if connection_type == 'sqlite':
        db_path = input("Ingresa la ruta del archivo SQLite: ")
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName('TestConnections.test_sqlite_connection'))
    elif connection_type == 'mysql':
        host = input("Ingresa el host de MySQL: ")
        database = input("Ingresa el nombre de la base de datos MySQL: ")
        user = input("Ingresa el usuario de MySQL: ")
        password = input("Ingresa la contraseña de MySQL: ")
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName('TestConnections.test_mysql_connection'))
    elif connection_type == 'oracledb':
        user = input("Ingresa el usuario de OracleDB: ")
        password = input("Ingresa la contraseña de OracleDB: ")
        dsn = input("Ingresa el DSN de OracleDB: ")
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName('TestConnections.test_oracledb_connection'))
    else:
        print("Opción no válida.")