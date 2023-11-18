import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from classesql import User
from databaseconnection import DBConnection
from PIL import Image, ImageTk
from levellogic import run_game
from sound import Sound


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry('768x735')
        self.root.title('Login')
        self.bgimage = Image.open(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\doorimage.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        canvas = tk.Canvas(self.root, width=768, height=735)
        canvas.pack()

        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.root.resizable(height=False, width=False)
        self.labeluser = tk.Label(self.root, text='username',bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.labeluser.place(x=250, y=180)
        self.entryuser = tk.Entry(self.root)
        self.entryuser.place(x=250, y=220)
        self.labelpass = tk.Label(self.root, text='password',bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.labelpass.place(x=250, y=260)
        self.entrypass = tk.Entry(self.root)
        self.entrypass.place(x=250, y=300)
        self.validbutton = tk.Button(self.root, text='GO!', bg='purple', fg='gold', font=('Small Fonts', 17,),command=self.login)
        self.validbutton.place(x=250, y=340)
        self.newuserbutton = tk.Button(self.root, text='New here, click here and subscribe!',bg='purple', fg='gold', font=('Small Fonts', 17,), command=self.goto_new_user_form)
        self.newuserbutton.place(x=250, y= 520)


    def goto_new_user_form(self):
        self.root.withdraw()
        root_new_user_form = tk.Toplevel(self.root)
        new_user_form = NewUserForm(root_new_user_form)
        new_user_form.run()

    def openstory1(self):
        self.root.withdraw()
        root_story1 = tk.Toplevel(self.root)
        new_user_form = Story1(root_story1)
        new_user_form.run()
    
    def login(self):
        databasecnx = DBConnection()
        valuser = self.entryuser.get()
        valpass = self.entrypass.get()

        if databasecnx.is_login_true(valuser, valpass):
            self.launch_game()
        else:
            messagebox.showerror('Error', 'Wrong username or password, stay focused!', parent=self.root)


    def launch_game(self):
        self.root.withdraw()  # Fermez la fenêtre de connexion
        # Démarrer le jeu ici
        run_game()  # Démarrage du jeu (ajustez selon vos besoins)

    def run(self):
        self.root.mainloop()

class Story1:
    def __init__(self, root):
        self.root = root
        self.root.geometry('768x728')
        self.root.title('Story')
        self.bgimage = Image.open(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\story1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        canvas = tk.Canvas(self.root, width=768, height=735)
        canvas.pack()

        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        self.validbutton = tk.Button(self.root, text='GO!', bg='purple', fg='gold', font=('Small Fonts', 17,),command=self.launch_game)
        self.validbutton.pack()
    def launch_game(self):
        self.root.withdraw()  # Fermez la fenêtre de connexion
        # Démarrer le jeu ici
        run_game()  # Démarrage du jeu (ajustez selon vos besoins)

class NewUserForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('768x728')
        self.root.title('New User Form')
        self.root.resizable(height=False, width=False)
        self.bgimage = Image.open(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\newuserformimage.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        canvas = tk.Canvas(self.root, width=768, height=728)
        canvas.pack()
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.titre = tk.Label(self.root,text="Master needs information about you",bg='purple', fg='gold', font=('Small Fonts', 18,))
        self.titre.place(x=75, y=140)

        self.username_label = tk.Label(self.root, text="Username",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.username_label.place(x=75, y=240)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x=300, y=245)

        self.password_label = tk.Label(self.root, text="Password",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.password_label.place(x=75, y=300)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.place(x=300, y=305)

        self.age_label = tk.Label(self.root, text="Age",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.age_label.place(x=75, y=340)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.place(x=300, y=345)

        self.email_label = tk.Label(self.root, text="Email",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.email_label.place(x=75, y=400)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.place(x=300, y=405)

        self.gender_label = tk.Label(self.root, text="Gender",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.gender_label.place(x=75, y=460)
        self.gender = tk.StringVar()
        self.gender_choose = ttk.Combobox(self.root, width=30, textvariable=self.gender)
        self.gender_choose['values'] = ('Male', 'Female', 'Both', 'Other')
        self.gender_choose.place(x=300, y=465)

        self.validbutton = tk.Button(self.root, text="SUBMIT", bg='purple', fg='gold', font=('Small Fonts', 15,),command=self.save)
        self.validbutton.place(x=400, y=500)

        self.gobackbutton = tk.Button(self.root, text="GO BACK", bg='purple', fg='gold', font=('Small Fonts', 15,),command=self.gotomainpage)
        self.gobackbutton.place(x=400, y=600)

            
            
    def save(self):
        databasecnx = DBConnection()
        valuser = self.username_entry.get()
        valpassw = self.password_entry.get()
        valage = self.age_entry.get()
        valemail = self.email_entry.get()
        valgender = self.gender_choose.get()
        if not self.is_username_unique(valuser):
            messagebox.showerror('Error', 'Username already exists', parent=self.root)
            return
        if not self.is_email_unique(valemail):
            messagebox.showerror('Error', 'Email already exists', parent=self.root)
            return

        else:
            databasecnx.adduser(User(valuser, valpassw, valage, valemail, valgender))
            self.root.withdraw()
            login_root = tk.Toplevel()
            app_login = Login(login_root)
            app_login.run()


    def is_username_unique(self, username):
        databasecnx = DBConnection()
        if databasecnx.is_username_exists(username):
            return False
        return True

    def is_email_unique(self, email):
        databasecnx = DBConnection()
        if databasecnx.is_email_exists(email):
            return False
        return True

    def run(self):
        self.root.mainloop()


root = tk.Tk()
app_login = Login(root)
app_login.run()

    







