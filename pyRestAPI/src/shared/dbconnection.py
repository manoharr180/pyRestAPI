import pyodbc


class DBConnection:
    def __init__(self):
        self.connection = self.get_db_conn()

    def __str__(self):
        return "DB_Connection"

    @staticmethod
    def get_db_conn():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-ABC123\\SQLEXPRESS;'
                              'Database=GeoLens;'
                              'Trusted_Connection=yes;')
        return conn

    def open_conn(self):
        return self.connection

    def discon_from_db(self):
        self.connection.close()
