import pygame
from random import randint
from explose import Explose
from projectiles import ProjectilesGoodelf


class BonusAttack(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 0
        self.image = pygame.image.load(r'image\elfbonusicone.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 380
        self.position_x = randint(200, (400 - self.rect.width))
        self.position_y = randint(250, 500)
        self.game = game
        self.health = 1 # Nombre de vies initiales
        self.maxhealth = self.health

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.bonusattack_sound.play()
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.spawngoodelf()
            self.game.bonusremain -= 1
            self.game.bonusattackspawn = False

class BonusMelee(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 0
        self.image = pygame.image.load(r'image\elfbonusicone.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 380
        self.position_x = randint(200, (400 - self.rect.width))
        self.position_y = randint(250, 500)
        self.game = game
        self.health = 1 # Nombre de vies initiales
        self.maxhealth = self.health

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.bonusattack_sound.play()
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.spawngoodelfsword()
            self.game.bonusremain -= 1
            self.game.bonusattackspawn = False

class GoodElf(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load(r'image\elfbonus.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 600
        self.position_x = randint(200, (400 - self.rect.width))
        self.position_y = randint(500, 550)
        self.projectilesgoodelf = ProjectilesGoodelf(self, game)
        self.allprojectilesgoodelf = pygame.sprite.Group()
        self.game = game
        self.health = 500 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 3
        self.shoot_cooldown = 1000  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.y > 600:
            self.rect.y = 600
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(120, (350 - self.rect.width))
           self.launchprojectilesenemy() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(400, 500)
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
            self.game.music.goodelf_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.remove()
            self.game.score -= 15
            self.game.bonusremain -=1
            print('bonusremain',self.game.bonusremain)
       



class GoodElfSword(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load(r'image\goodelfsword.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100,400)
        self.rect.y = 600
        self.position_x = randint(100, (400 - self.rect.width))
        self.position_y = randint(1, 400)
        self.game = game
        self.health = 600 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 6
        self.shoot_cooldown = 1400  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        enemies_hit = pygame.sprite.spritecollide(self, self.game.allenemies, False)
        for enemy in enemies_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit enemy')

        peon_hit = pygame.sprite.spritecollide(self, self.game.allpeon, False)
        for enemy in peon_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit peon')

        enemies_boat_hit= pygame.sprite.spritecollide(self, self.game.allenemiesonaboat, False)
        for enemy in enemies_boat_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit boat')

        warg_hit=pygame.sprite.spritecollide(self, self.game.allwarg, False)
        for enemy in warg_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit warg')
        
        dwarf_hit=pygame.sprite.spritecollide(self, self.game.alldwarf, False)
        for enemy in dwarf_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit dwarf')


        gobelinarcher_hit=pygame.sprite.spritecollide(self, self.game.allgobelinarcher, False)
        for enemy in gobelinarcher_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit gobelinarcher')

        gobelinmassue_hit=pygame.sprite.spritecollide(self, self.game.allgobelinmassue, False)
        for enemy in gobelinmassue_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.attack)
            print('melee hit gobelinmassue')


        boss_hit = pygame.sprite.spritecollide(self, self.game.allboss, False)
        for boss in boss_hit:
            # Réduisez la vie du boss en fonction de l'attaque du joueur
            boss.damage(self.attack)
            print('melee hit boss')


        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(100, (460 - self.rect.width))
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(1, 400)

    def hit(self):
        if self.game.enemy.health > 1:
            self.game.enemy.damage(self.attack)

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
            self.game.music.goodelf_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.remove()
            self.game.score -= 15
            self.game.bonusremain -=1
            print('bonusremain',self.game.bonusremain)
       
