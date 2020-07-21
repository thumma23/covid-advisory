import mysql.connector as mysql
import db

user_db = mysql.connect(
    host = db.database_cfg['host'],
    user = db.database_cfg['user'],
    passwd = db.database_cfg['passwd'],
    database = db.database_cfg['database']
)

db_cursor = user_db.cursor()
class Users_DB():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        sql = "INSERT into users (username, password) VALUES (%s, %s)"
        val = (self.username, self.password)
        db_cursor.execute(sql, val)
        user_db.commit()
    
    def findUsername(self):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (self.username, self.password)
        db_cursor.execute(sql, val)
        return db_cursor.fetchall()[0]
    
    def findID(self, user_id):
        sql = "SELECT * FROM users WHERE id = %s"
        val = (user_id,)
        db_cursor.execute(sql, val)
        return db_cursor.fetchall()[0]
    
    
    


