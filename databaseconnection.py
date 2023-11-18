import mysql.connector
from classesql import User

class DBConnection():
    userid = ''
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
                    user.append(User(row[1],row[2], row[3], row[4], row[5],row[6]))
            #self.connection.close()
            self.lastmessage = "Lecture terminée"
        else:
            self.lastmessage = "Could not connect"
        return user
    def finduserdic(self):
        users = {}
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                print('DBuserid-finuserdic', DBConnection.userid)#ok

                cursor.execute(f"SELECT * FROM Endof4age WHERE username = '{DBConnection.userid}' LIMIT 1")
                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        print(row)#ok
                        user_data = {
                            'username': row[1],
                            'passw': row[2],
                            'age': row[3],
                            'email': row[4],
                            'gender': row[5],
                            'highscore': row[6]
                        }
                        users = user_data
                else:
                    print("Aucun enregistrement trouvé")

                self.lastmessage = "Lecture terminée"
        else:
            self.lastmessage = "Could not connect"
        print('DB-finduserdic()', users)
        return users

    def adduser(self, user: User):
        resultat = 0
        if self.connection and self.connection.is_connected():
            with self.connection.cursor() as cursor:
                cursor.execute(("INSERT INTO Endof4age (username, passw, age, email, gender, highscore) "
                                        "VALUES (%s, %s, %s, %s, %s, %s)"),
                                        (user.username, user.passw, user.age,
                                         user.email, user.gender, user.highscore))
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
                    DBConnection.userid = username
                    print('DBuserid',DBConnection.userid, 'username',username)
                    return True  # L'utilisateur est authentifié
        return False  # L'authentification a échoué
    
    def executed(self, query, params=None):
        result = None
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchone()  # Utilisez fetchone pour obtenir la première ligne
        except Exception as e:
            print(f"Error executing query: {e}")
        return result[0] if result else None


    def savehighscore(self, username, current_Score=0):
        query_select = "SELECT highscore FROM Endof4age WHERE username = %s"
        query_update = "UPDATE Endof4age SET highscore = %s WHERE username = %s;"
        DBConnection.userid = username

        # Exécutez la requête SELECT pour obtenir le score actuel de l'utilisateur.
        current_score = self.executed(query_select, (username,))
        if current_score is not None:
            try:
                current_score = int(current_score)  # Convertir en entier
            except (ValueError, TypeError):
                print(f"Error converting highscore to int: {current_score}")
                return

        # Assurez-vous que user.highscore est un entier avant d'essayer de l'insérer dans la base de données.
        try:
            print('currentScore', current_Score)
            int_score = int(current_Score)
        except ValueError:
            print(f"Error converting user's highscore to int: {current_Score}")
            return

        # Vérifiez si le nouveau score est supérieur au score actuel.
        if current_score is None or int_score > current_score:
            # Mettez à jour le nouveau score.
            print('intscore', int_score, username, query_update)
            self.executed(query_update, (int_score, username))

            # Assurez-vous que vous avez une méthode commit dans votre classe DBConnection pour appliquer les modifications à la base de données.
            self.connection.commit()
            print('HS updated')