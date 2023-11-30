import sqlite3
from classesql import User
import bcrypt

class DBConnection():
    userid = ''

    def __init__(self):
        try:
            self.connection = sqlite3.connect('datatest.db')
            self.create_table()
            self.lastmessage = "Connection successful"
        except Exception as exception:
            self.lastmessage = str(exception)

    def __del__(self):
        try:
            self.connection.close()
            self.lastmessage = "Connection closed"
        except Exception as e:
            self.lastmessage = str(e)

    def create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Endof4age (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                passw TEXT NOT NULL,
                age INTEGER,
                email TEXT,
                gender TEXT,
                highscore INTEGER
            );
        '''
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(create_table_query)
            self.lastmessage = "Table created successfully"
        except sqlite3.Error as e:
            self.lastmessage = f"Error during table creation: {e}"

    def finduser(self):
        user = []
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT * FROM Endof4age")
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                        user.append(User(row[1], row[2], row[3], row[4], row[5], row[6]))
                self.lastmessage = "Lecture terminée"
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
        else:
            self.lastmessage = "Could not connect"
        return user

    def finduserdic(self):
        users = {}
        if self.connection:
            try:
                with self.connection:
                    print('DBuserid-finuserdic', DBConnection.userid)
                    cursor = self.connection.cursor()
                    cursor.execute(f"SELECT * FROM Endof4age WHERE username = ? LIMIT 1", (DBConnection.userid,))
                    rows = cursor.fetchall()

                    if rows:
                        for row in rows:
                            print(row)
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
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
        else:
            self.lastmessage = "Could not connect"
        return users

    def adduser(self, user: User):
        resultat = 0
        if self.connection:
            try:
                with self.connection:
                    hashed_password = bcrypt.hashpw(user.passw.encode('utf-8'), bcrypt.gensalt())
                    cursor = self.connection.cursor()
                    cursor.execute(("INSERT INTO Endof4age (username, passw, age, email, gender, highscore) "
                                    "VALUES (?, ?, ?, ?, ?, ?)"),
                                    (user.username, hashed_password, user.age,
                                    user.email, user.gender, user.highscore))
                    resultat = cursor.lastrowid
                self.lastmessage = "insertion terminée"
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
                print(f"Error during query execution: {e}")
        else:
            self.lastmessage = "Could not connect"
        return resultat

    def is_username_exists(self, username):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM Endof4age WHERE username = ?", (username,))
                    result = cursor.fetchone()
                    if result and result[0] > 0:
                        return True  
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
        return False  
    
    def is_email_exists(self, email):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM Endof4age WHERE email = ?", (email,))
                    result = cursor.fetchone()
                    if result and result[0] > 0:
                        return True  
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
        return False 
    def is_login_true(self, username, password):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute('SELECT passw FROM Endof4age WHERE username = ?', (username,))
                    result = cursor.fetchone()

                    if result:
                        hashed_password = result[0]

                        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                            DBConnection.userid = username
                            return True
            except sqlite3.Error as e:
                self.lastmessage = f"Error during query execution: {e}"
        return False 

    def executed(self, query, params=None):
        result = None
        try:
            with self.connection:
                cursor = self.connection.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchone() 
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        return result[0] if result else None

    def savehighscore(self, username, current_Score=0):
        query_select = "SELECT highscore FROM Endof4age WHERE username = ?"
        query_update = "UPDATE Endof4age SET highscore = ? WHERE username = ?;"
        DBConnection.userid = username

        current_score = self.executed(query_select, (username,))
        if current_score is not None:
            try:
                current_score = int(current_score) 
            except (ValueError, TypeError):
                print(f"Error converting highscore to int: {current_score}")
                return

        try:
            int_score = int(current_Score)
        except ValueError:
            print(f"Error converting user's highscore to int: {current_Score}")
            return

        if current_score is None or int_score > current_score:
            self.executed(query_update, (int_score, username))
            self.connection.commit()
