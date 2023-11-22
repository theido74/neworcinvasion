import pygame
import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar, Frame, Button
from PIL import Image, ImageTk


class Text:
    def __init__(self,screen):
        self.screen = screen          
def show_text_window(screen, text):
    font = pygame.font.Font(r'police\small_pixel.ttf', 14)
    text_surface = font.render(text, True, 'purple', 'gold')
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def wait_for_key_press(key):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == key:
                    waiting = False


def show_image(screen, image_path, x, y):
    try:
        image = pygame.image.load(image_path).convert_alpha()
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return

    # Obtenir la nouvelle taille en pourcentage
    width = int(image.get_width() * 25 / 100)
    height = int(image.get_height() * 25 / 100)
    resized_image = pygame.transform.scale(image, (width, height))
    image_rect = resized_image.get_rect()

    # Définir les coordonnées de l'image
    image_rect.x = x
    image_rect.y = y

    screen.blit(resized_image, image_rect)
    pygame.display.flip()


class Story2:
    def __init__(self, root, image_path):
        self.root = root
        self.root.geometry('789x530')
        self.root.title('Story')
        self.root.resizable(height=False, width=False)

        container = Frame(self.root)
        container.pack(fill="both", expand=True)

        # Récupérer la hauteur totale de l'écran
        screen_height = self.root.winfo_screenheight()

        self.bgimage = Image.open(image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bgimage)

        self.canvas = Canvas(container, width=768, height=528)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        style = ttk.Style()
        style.configure("Vertical.TScrollbar", troughcolor="purple", bordercolor="gold", arrowcolor="green")
        scrollbar = ttk.Scrollbar(container, command=self.canvas.yview, style="Vertical.TScrollbar")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.config(yscrollcommand=scrollbar.set)
        
        self.validbutton = Button(self.canvas, text='GO!', bg='purple', fg='gold', font=('Small Fonts', 13), command=self.root.destroy)
        self.validbutton_window = self.canvas.create_window(710, 490, window=self.validbutton, anchor='ne')


    def run(self):
        self.root.mainloop()
