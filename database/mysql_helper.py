import mysql.connector
from config.config import MYSQL_CONFIG

class MySQLHelper:
    
    def _execute(self, sql, params=None):
        conn = mysql.connector.connect(
            **MYSQL_CONFIG
        )
        cursor = conn.cursor(
            dictionary = True
        )
        cursor.execute(sql, params)
        return conn, cursor

    def query(self, sql, params=None):
        conn, cursor = self._execute(sql, params)
        try:
            result = cursor.fetchall()
            return result
        
        finally:
            cursor.close()
            conn.close()
    
    def query_one(self, sql, params=None):
        conn, cursor = self._execute(sql, params)
        try:
            result = cursor.fetchone()
            return result
        
        finally:
            cursor.close()
            conn.close()