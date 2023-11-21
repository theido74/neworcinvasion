import pygame

class Text:
    def __init__(self,screen):
        self.screen = screen          
def show_text_window(screen, text):
    font = pygame.font.Font(r'c:\Users\ponce\AppData\Local\Microsoft\Windows\Fonts\small_pixel.ttf', 14)
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

