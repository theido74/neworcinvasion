class User:
    def __init__(self, username, passw, age, email, gender, highscore = 0):

        self.username = username
        self.passw = passw
        self.age = age
        self.email = email
        self.gender = gender
        self.highscore = highscore

    def creatspell(self):
        print (self.username, "is born")
    
    def __str__(self):
        return str(self.username).upper()

