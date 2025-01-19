import mysql.connector
from mysql.connector import Error
import streamlit as st

def get_connection():
    """Membuat koneksi ke database MySQL menggunakan Streamlit Secrets."""
    try:
        conn = mysql.connector.connect(
            host=st.secrets["DB_HOST"],          # Host database
            database=st.secrets["DB_DATABASE"],  # Nama database
            user=st.secrets["DB_USER"],          # Username database
            password=st.secrets["DB_PASSWORD"]   # Password database
        )
        return conn
    except Error as e:
        st.error(f"Error saat menyambungkan ke database: {e}")
        return None
