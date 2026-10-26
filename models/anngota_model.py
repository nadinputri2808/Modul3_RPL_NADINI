import mysql.connector
from config.database import db_config

class AnggotaModel:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all_anggota(self):
        query = "SELECT * FROM anggota"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_anggota(self, nama, email, telepon):
        try:
            query = "INSERT INTO anggota (nama, email, telepon) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (nama, email, telepon))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False