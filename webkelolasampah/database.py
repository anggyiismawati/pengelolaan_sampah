import mysql.connector
from mysql.connector import Error

def get_connection():
    """Membuat koneksi ke database MySQL."""
    try:
        conn = mysql.connector.connect(
            host='https://mobilecomputing.my.id:2083/',        # Ganti dengan host MySQL Anda
            database='mobw7774_kelola_sampah',  # Ganti dengan nama database Anda
            user='mobw7774',             # Ganti dengan username MySQL Anda
            password='HucgKZPcExj467'   # Ganti dengan password MySQL Anda
        )
        return conn
    except Error as e:
        print(f"Error saat menyambungkan ke database: {e}")
        return None
