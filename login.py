import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, Canvas, Scrollbar, Frame, Button
from classesql import User
from databaseconnection import DBConnection
from PIL import Image, ImageTk
from levellogic import run_game
from sound import Sound

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry('789x530')
        self.root.title('Login')
        self.bgimage = Image.open(r'image\doorimage.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)
        self.root.resizable(height=False, width=False)

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
        self.entrypass = tk.Entry(self.root, show='*')
        self.entrypass.place(x=250, y=300)
        self.validbutton = tk.Button(self.root, text='GO!', bg='purple', fg='gold', font=('Small Fonts', 17,),command=self.login)
        self.validbutton.place(x=250, y=340)
        self.newuserbutton = tk.Button(self.root, text='New here, click here and subscribe!',bg='purple', fg='gold', font=('Small Fonts', 17,), command=self.goto_new_user_form)
        self.newuserbutton.place(x=250, y= 400)


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
            self.openstory1()
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
        self.root.geometry('789x530')
        self.root.title('Story')
        self.root.resizable(height=False, width=False)

        container = Frame(self.root)
        container.pack(fill="both", expand=True)

        # Récupérer la hauteur totale de l'écran
        screen_height = self.root.winfo_screenheight()

        self.bgimage = Image.open(r'image\story1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        self.canvas = Canvas(container, width=768, height=528)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        style = ttk.Style()
        style.configure("Vertical.TScrollbar", troughcolor="lightgrey", bordercolor="grey", arrowcolor="black")
        scrollbar = ttk.Scrollbar(container, command=self.canvas.yview, style="Vertical.TScrollbar")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.validbutton = Button(self.canvas, text='GO!', bg='purple', fg='gold', font=('Small Fonts', 17), command=self.launch_game)
        self.validbutton_window = self.canvas.create_window(self.canvas.winfo_reqwidth() - 200, screen_height - 30, window=self.validbutton, anchor='ne')

        # Ajouter la molette de la souris pour faire défiler le contenu du canevas
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.root.bind("<KeyRelease>", self.on_mousewheel)

    def launch_game(self):
        self.root.withdraw()  # Fermer la fenêtre de connexion
        # Démarrer le jeu ici
        run_game()  # Démarrage du jeu (ajustez selon vos besoins)

    def on_mousewheel(self, event):
        # Récupérer la quantité de défilement
        delta = int(-1 * (event.delta / 120))

        # Récupérer les coordonnées du haut et du bas
        canvas_top = self.canvas.canvasy(0)
        canvas_bottom = canvas_top + self.canvas.winfo_height()
        window_top = 0
        window_bottom = self.root.winfo_height()

        # Empêcher le défilement vers le haut ou le bas si le haut du canevas est déjà visible
        if delta > 0 and canvas_top-190 <= window_top:
            self.canvas.yview_scroll(delta, "units")
        elif delta < 0 and canvas_bottom-1 >= window_bottom:
            self.canvas.yview_scroll(delta, "units")




class NewUserForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('789x530')
        self.root.title('New User Form')
        self.root.resizable(height=False, width=False)
        self.bgimage = Image.open(r'image\newuserform.png')
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        canvas = tk.Canvas(self.root, width=768, height=728)
        canvas.pack()
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.titre = tk.Label(self.root,text="Master needs information about you",bg='purple', fg='gold', font=('Small Fonts', 18,))
        self.titre.place(x=75, y=30)

        self.username_label = tk.Label(self.root, text="Username",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.username_label.place(x=75, y=120)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x=300, y=125)

        self.password_label = tk.Label(self.root, text="Password",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.password_label.place(x=75, y=165)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.place(x=300, y=170)

        self.age_label = tk.Label(self.root, text="Age",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.age_label.place(x=75, y=210)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.place(x=300, y=215)

        self.email_label = tk.Label(self.root, text="Email",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.email_label.place(x=75, y=245)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.place(x=300, y=250)

        self.gender_label = tk.Label(self.root, text="Gender",bg='purple', fg='gold', font=('Small Fonts', 15,))
        self.gender_label.place(x=75, y=290)
        self.gender = tk.StringVar()
        self.gender_choose = ttk.Combobox(self.root, width=30, textvariable=self.gender)
        self.gender_choose['values'] = ('Male', 'Female', 'Both', 'Other')
        self.gender_choose.place(x=300, y=295)

        self.validbutton = tk.Button(self.root, text="SUBMIT", bg='purple', fg='gold', font=('Small Fonts', 15,),command=self.save)
        self.validbutton.place(x=400, y=400)

        self.gobackbutton = tk.Button(canvas, text="GO BACK", bg='purple', fg='gold', font=('Small Fonts', 15,),command=self.goto_main)
        self.gobackbutton.place(x=500, y=400)

            
    def goto_main(self):
        self.root.withdraw()
        root_main = tk.Toplevel(self.root)
        new_user_form = Login(root_main)
        new_user_form.run()

    
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

    







