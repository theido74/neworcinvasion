import mysql.connector
from classesql import User

class DBConnection():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(user='root', password='LaCasita2022',
                                          host='127.0.0.1',
                                          database='datatest')
            self.lastmessage = "Connection successful"
        except Exception as exception:
            self.lastmessage = str(exception)

    def __del__(self):
        try:
            self.connection.close()
            self.lastmessage = "Connection closed"
        except Exception as e:
            self.lastmessage = str(e)

    def finduser(self):
        user = []
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Endof4age")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                    user.append(User(row[1],row[2], row[3], row[4], row[5],))
            #self.connection.close()
            self.lastmessage = "Lecture terminée"
        else:
            self.lastmessage = "Could not connect"
        return user
    
    def adduser(self, user: User):
        resultat = 0
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute(("INSERT INTO Endof4age (username, passw, age, email, gender) "
                                        "VALUES (%s, %s, %s, %s, %s)"),
                                        (user.username, user.passw, user.age,
                                         user.email, user.gender))
                self.connection.commit()
                resultat = cursor.lastrowid
            self.lastmessage = "insertion terminée"
        else:
            self.lastmessage = "Could not connect"
        return resultat
    
    def is_username_exists(self, username):
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Endof4age WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result and result[0] > 0:
                    return True  # Le nom d'utilisateur existe 
        return False  # Le nom d'utilisateur est unique

    def is_email_exists(self, email):
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Endof4age WHERE email = %s", (email,))
                result = cursor.fetchone()
                if result and result[0] > 0:
                    return True  # L'e-mail existe 
        return False  # L'e-mail est unique
    
    def is_login_true(self, username, passw):
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT COUNT(username) FROM Endof4age WHERE username = %s AND passw = %s', (username, passw))
                result = cursor.fetchone()
                if result and result[0] > 0:
                    return True  # L'utilisateur est authentifié
        return False  # L'authentification a échoué
  