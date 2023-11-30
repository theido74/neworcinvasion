import pygame
from projectiles import Projectiles, ProjectilesEnemy

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(r'image\gandalfplayer.png')
        self.rect = self.image.get_rect()
        self.rect.x = 170
        self.rect.y = 600
        self.game = game
        self.velocity = 5
        self.projectile = Projectiles(self, game)
        self.allprojectiles = pygame.sprite.Group()
        self.health = 350 
        self.maxhealth = self.health
        self.attack = 25


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


    def kill(self):
        super().kill()
    
    def killplayer(self):
        self.health -= 1
        if self.health <= 0:
            print('Game Over')
    
    def updatehealthbar(self, surface):
        bar_color = (71, 209, 71)
        bg_bar_color = (230, 0, 0)
        bar_height = 5
        max_bar_width = 120
        bar_width = int(min(self.health / self.maxhealth * self.rect.width, max_bar_width))
        bar_position = [self.rect.x + (self.rect.width - bar_width) // 2, self.rect.y + self.rect.height, bar_width, bar_height]
        bg_bar_position = [self.rect.x, self.rect.y + self.rect.height, self.rect.width, bar_height]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.killplayer()
            self.game.gameover()
            self.game.enemyremain = 0
