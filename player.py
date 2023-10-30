import pygame
from projectiles import Projectiles, ProjectilesEnemy

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\gandalfperso copie.png')
        self.rect = self.image.get_rect()
        self.rect.x = 170
        self.rect.y = 600
        self.game = game
        self.velocity = 5
        self.projectile = Projectiles(self, game)
        self.allprojectiles = pygame.sprite.Group()
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 5


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity

    def launchprojectile(self):
        self.game.music.shoot_sound.play()
        self.allprojectiles.add(Projectiles(self, self.game))



    def remove(self):
        self.game.allplayer.remove(self)
    
    def kill(self):
        self.health -= 1
        if self.health <= 0:
            print('Game Over')
    
    def updatehealthbar(self, surface):
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x - 5, self.rect.y + self.rect.height, self.health, 5]
        bgbarposition = [self.rect.x - 5, self.rect.y + self.rect.height, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            self.game.gameover()
            