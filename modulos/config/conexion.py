import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='boqicridrlrqfp7wqp0w-mysql.services.clever-cloud.com',
            user='urccnva9ugksvokl',
            password='rpt9b2B6Rqlj1PU5W0VI',
            database='boqicridrlrqfp7wqp0w',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
