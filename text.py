import pygame
import tkinter as tk
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
    width = int(image.get_width() * 22 / 100)
    height = int(image.get_height() * 22 / 100)
    resized_image = pygame.transform.scale(image, (width, height))
    image_rect = resized_image.get_rect()

    # Définir les coordonnées de l'image
    image_rect.x = x
    image_rect.y = y

    screen.blit(resized_image, image_rect)
    pygame.display.flip()





