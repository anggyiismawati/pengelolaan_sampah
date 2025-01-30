import mysql.connector
from mysql.connector import Error
import streamlit as st

def get_connection():
    """Membuat koneksi ke database MySQL menggunakan Streamlit Secrets."""
    try:
        conn = mysql.connector.connect(
            host='mobilecomputing.my.id',          # Host database
            database='mobw7774_kelola_sampah',  # Nama database
            user='mobw7774_anggy',          # Username database
            password='Skripsi2025!'   # Password database
        )
        return conn
    except Error as e:
        st.error(f"Error saat menyambungkan ke database: {e}")
        return None
