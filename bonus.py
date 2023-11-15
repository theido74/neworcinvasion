import pygame
from random import randint
from explose import Explose
from projectiles import ProjectilesGoodelf


class BonusAttack(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 0
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\elfbonus.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(200, (400 - self.rect.width))
        self.position_y = randint(250, 500)
        self.game = game
        self.health = 1 # Nombre de vies initiales
        self.maxhealth = self.health

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.explose_sound.play()
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()

class GoodElf(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 1.8
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\elfbonus.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 600
        self.position_x = randint(200, (400 - self.rect.width))
        self.position_y = randint(500, 550)
        self.projectilesgoodelf = ProjectilesGoodelf(self, game)
        self.allprojectilesgoodelf = pygame.sprite.Group()
        self.game = game
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 15
        self.shoot_cooldown = 800  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.y > 600:
            self.rect.y = 600
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(200, (460 - self.rect.width))
           self.launchprojectilesenemy() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(400, 400)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesgoodelf.add(ProjectilesGoodelf(self, self.game))        
    
    def launchprojectilesenemy(self):
        self.allprojectilesgoodelf.add(ProjectilesGoodelf(self, self.game))

    def kill(self):
        super().kill()

    def updatehealthbar(self, surface):
        bar_color = (71, 209, 71)
        bg_bar_color = (230, 0, 0)
        bar_height = 5
        max_bar_width = 120

        # Calcul de la position et de la largeur pour la barre de santé
        bar_width = int(min(self.health / self.maxhealth * self.rect.width, max_bar_width))
        bar_position = [self.rect.x + (self.rect.width - bar_width) // 2, self.rect.y + self.rect.height, bar_width, bar_height]
        bg_bar_position = [self.rect.x, self.rect.y + self.rect.height, self.rect.width, bar_height]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.explose_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score -= 15
            self.game.bonusremain -=1
            print(self.game.bonusremain)
       
    def remove(self):
        self.game.remove(self)