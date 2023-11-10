import pygame

class Explose(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()  # Vous avez oublié les parenthèses ici
        self.images = loadanimation()  # Assurez-vous d'appeler votre fonction loadanimation pour obtenir la liste d'images
        self.image = self.images[0]  # Initialisez l'image avec la première image de l'animation
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.currentimg = 0
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.currentimg += 1
            if self.currentimg >= len(self.images):
                self.currentimg = 0
                if not loop:
                    self.animation = False
            self.image = self.images[self.currentimg]

def loadanimation():
    images = []
    path = r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\ressource\ressource\explose\explose'
    for num in range(1, 46):
        image_path = path + str(num) + '.png'
        img = pygame.image.load(image_path)
        imgscale = pygame.transform.scale(img, (80, 80))
        images.append(imgscale)
    return images

animations = {
    'explose': loadanimation()
}
