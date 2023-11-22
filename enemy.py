import pygame
from pygame.math import Vector2
from random import randint
from projectiles import Projectiles,ProjectilesEnemy, ProjectilesBoss, ProjectilesEnemyOnaBoat, ProjectilesBossBoat, ProjectilesWargPoison, ProjectilesBossWarg,ProjectilesDwarf, ProjectilesBossDwarf,ProjectilesGobelinArcher, ProjectilesGobelinMassue, ProjectilesBalrog
from explose import Explose
from player import Player

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 1.8
        self.image = pygame.image.load(r'image\orcenemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileenemy = ProjectilesEnemy(self, game)
        self.allprojectilesenemy = pygame.sprite.Group()
        self.game = game
        self.health = 275 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 5
        self.shoot_cooldown = 1000  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir
        self.boss = Boss

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesenemy() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 300)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesenemy.add(ProjectilesEnemy(self, self.game))        
    
    def launchprojectilesenemy(self):
        self.allprojectilesenemy.add(ProjectilesEnemy(self, self.game))

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
            self.remove()
            self.game.score += 15
            self.game.enemyremain -=1
            print('enemy killed-enemyremain ',self.game.enemyremain)
       
  


class Peon(Enemy,pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 3
        self.image = pygame.image.load(r'image\peon.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 700)
        self.allpeon = pygame.sprite.Group()
        self.game = game
        self.health = 100 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        # Vérifier la proximité du joueur
        distance_to_player = pygame.math.Vector2(self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y).length()
        if distance_to_player < 50:  # Ajustez la distance d'attaque au besoin
            self.hit()
        # Calculer le vecteur de direction vers le joueur
        direction = Vector2(self.game.player.rect.x+1 - self.rect.x+1, self.game.player.rect.y+1 - self.rect.y+1).normalize()

        # Déplacer l'ennemi dans la direction du joueur
        self.rect.x += direction.x * self.velocity
        self.rect.y += direction.y * self.velocity

    def hit(self):
        if self.game.player.health > 1:
            self.game.player.damage(self.attack)
        if self.game.goodelf.health > 1:
            self.game.goodelf.damage(self.attack)
        if self.game.goodelfsword.health > 1:
            self.game.goodelfsword.damage(self.attack)
        

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
            self.game.music.peon_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.remove()
            self.game.score += 1
            self.game.enemyremain -=1
            print('peon killed', self.game.enemyremain)




class EnemyOnBoat(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.8
        self.image = pygame.image.load(r'image\orconaaboat.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileenemyonaboat = ProjectilesEnemyOnaBoat(self, game)
        self.allprojectilesenemyonaboat = pygame.sprite.Group()
        self.allenemiesonaboat = pygame.sprite.Group()
        self.game = game
        self.health = 400 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1600  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width/2))
           self.launchprojectilesenemyonaboat() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 550)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesenemyonaboat.add(ProjectilesEnemyOnaBoat(self, self.game))        
    
    def launchprojectilesenemyonaboat(self):
        self.allprojectilesenemyonaboat.add(ProjectilesEnemyOnaBoat(self, self.game))

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
            self.game.music.boat_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1
            print('enemyonboat killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyWarg(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 3
        self.image = pygame.image.load(r'image\wargenemy.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileswargpoison = ProjectilesWargPoison(self, game)
        self.allprojectileswargpoison = pygame.sprite.Group()
        self.allwarg = pygame.sprite.Group()
        self.game = game
        self.health = 500 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 6
        self.shoot_cooldown = 1200  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        player_hit = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in player_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            player.damage(self.attack)
        goodelf_hit = pygame.sprite.spritecollide(self, self.game.allgoodelf, False)
        for goodelf in goodelf_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            goodelf.damage(self.attack)
        goodelfsword_hit = pygame.sprite.spritecollide(self, self.game.allgoodelfsword, False)
        for goodelfsword in goodelfsword_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            goodelfsword.damage(self.attack)
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectileswargpoison() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 500)
        self.check_shoot()


    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectileswargpoison.add(ProjectilesWargPoison(self, self.game))        
    
    def launchprojectileswargpoison(self):
        self.allprojectileswargpoison.add(ProjectilesWargPoison(self, self.game))

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
            self.game.music.warg_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 9
            self.game.enemyremain -=1
            print('warg killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyDwarf(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 1.5
        self.image = pygame.image.load(r'image\nainenemy.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x =  randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectiledwarf = ProjectilesDwarf(self, game)
        self.allprojectiledwarf = pygame.sprite.Group()
        self.alldwarf = pygame.sprite.Group()
        self.game = game
        self.health = 600 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 4
        self.shoot_cooldown = 1800  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (350 - self.rect.width))
           self.launchprojectilesdwarf() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 300)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectiledwarf.add(ProjectilesDwarf(self, self.game))        
    
    def launchprojectilesdwarf(self):
        self.allprojectiledwarf.add(ProjectilesDwarf(self, self.game))

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
            self.game.music.dwarf_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 12
            self.game.enemyremain -=1
            print('dwarf killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyGobelinArcher(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 1.5
        self.image = pygame.image.load(r'image\gobelinarcher.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x =  randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 200)
        self.projectilegobelinarcher = ProjectilesGobelinArcher(self, game)
        self.allprojectilesgobelinarcher = pygame.sprite.Group()
        self.allgobelinarcher = pygame.sprite.Group()
        self.game = game
        self.health = 200 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
        self.shoot_cooldown = 300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesgobelinarcher() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 200)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesgobelinarcher.add(ProjectilesGobelinArcher(self, self.game))        
    
    def launchprojectilesgobelinarcher(self):
        self.allprojectilesgobelinarcher.add(ProjectilesGobelinArcher(self, self.game))

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
            self.game.music.warg_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1
            print('gobelinarcher killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyGobelinMassue(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 4
        self.image = pygame.image.load(r'image\gobelinmassue.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 500)
        self.projectilegobelinmassue = ProjectilesGobelinMassue(self, game)
        self.allprojectilesgobelinmassue = pygame.sprite.Group()
        self.allgobelinmassue = pygame.sprite.Group()
        self.game = game
        self.health = 300 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        # Vérifier la proximité du joueur
        distance_to_player = pygame.math.Vector2(self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y).length()
        if distance_to_player < 50:  # Ajustez la distance d'attaque au besoin
            self.hit()
        # Calculer le vecteur de direction vers le joueur
        direction = Vector2(self.game.player.rect.x+1 - self.rect.x+1, self.game.player.rect.y+1 - self.rect.y+1).normalize()

        # Déplacer l'ennemi dans la direction du joueur
        self.rect.x += direction.x * self.velocity
        self.rect.y += direction.y * self.velocity

    def hit(self):
        if self.game.player.health > 1:
            self.game.player.damage(self.attack)
        if self.game.goodelf.health > 1:
            self.game.goodelf.damage(self.attack)
        if self.game.goodelfsword.health > 1:
            self.game.goodelfsword.damage(self.attack)


    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesgobelinmassue.add(ProjectilesGobelinMassue(self, self.game))        
    
    def launchprojectilesgobelinmassue(self):
        self.allprojectilesgobelinmassue.add(ProjectilesGobelinMassue(self, self.game))

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
            self.game.music.warg_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1
            print('gobelinmassue killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class Boss(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.7
        self.image = pygame.image.load(r'image\orcboss.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 150)
        self.projectileboss = ProjectilesBoss(self, game)
        self.allprojectilesboss = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 700 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 5
        self.shoot_cooldown = 2000  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):

        if self.rect.x < self.position_x:
            self.rect.x += self.velocity 
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity 
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesenemy() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity 
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity 
        if abs(self.rect.y - self.position_y) < self.velocity/2:
           self.position_y = randint(0, 150)
        self.check_shoot()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.explose_boss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.remove()
            self.game.score += 25 
            self.game.enemyremain -=1
            print('boss killed', self.game.enemyremain)

    def launchprojectilesboss(self):
        self.allprojectilesboss.add(ProjectilesBoss(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesboss.add(ProjectilesBoss(self, self.game))        

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


class BossBoat(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.7
        self.image = pygame.image.load(r'image\bossorcboat.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 180)
        self.projectilebossboat = ProjectilesBossBoat(self, game)
        self.allprojectilesbossboat = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 2500 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 10
        self.shoot_cooldown = 2000  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.y > 150:
            self.rect.y = 150
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesenemy() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity/2
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 180)
        self.check_shoot()

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

    def launchprojectilesboss(self):
        self.allprojectilesbossboat.add(ProjectilesBossBoat(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesbossboat.add(ProjectilesBossBoat(self, self.game))        

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



class BossWarg(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.6
        self.image = pygame.image.load(r'image\bossorcwarg.png')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 450)
        self.projectilebosswarg = ProjectilesBossWarg(self, game)
        self.allprojectilesbosswarg = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 2200 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 8
        self.shoot_cooldown = 3500  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        player_hit = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in player_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            player.damage(self.attack)
        goodelf_hit = pygame.sprite.spritecollide(self, self.game.allgoodelf, False)
        for goodelf in goodelf_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            goodelf.damage(self.attack)
        goodelfsword_hit = pygame.sprite.spritecollide(self, self.game.allgoodelfsword, False)
        for goodelfsword in goodelfsword_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            goodelfsword.damage(self.attack)
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (450 - self.rect.width))
           self.launchprojectilesboss() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 450)
        self.check_shoot()


    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.wargboss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 25 
            self.game.enemyremain -=1
            print('boss warg killed', self.game.enemyremain)

    def launchprojectilesboss(self):
        self.allprojectilesbosswarg.add(ProjectilesBossWarg(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesbosswarg.add(ProjectilesBossWarg(self, self.game))        

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



class BossDwarf(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.6
        self.image = pygame.image.load(r'image\bossnainenemy.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilebossdwarf = ProjectilesBossDwarf(self, game)
        self.allprojectilesbossdwarf = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 2500 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 13
        self.shoot_cooldown = 2500  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesboss() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity/2:
           self.position_y = randint(0, 250)
        self.check_shoot()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.dwarfboss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 25 
            self.game.enemyremain -=1
            print('boss dwarf killed', self.game.enemyremain)

    def launchprojectilesboss(self):
        self.allprojectilesbossdwarf.add(ProjectilesBossDwarf(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesbossdwarf.add(ProjectilesBossDwarf(self, self.game))        

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

class BossBalrog(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 2
        self.image = pygame.image.load(r'image\balrog.png')
        self.image = pygame.transform.scale(self.image, (250, 220))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilebossbalrog = ProjectilesBalrog(self, game)
        self.allprojectilesbossbalrog = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 2000 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 40
        self.shoot_cooldown = 2500  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesboss() 
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 250)
        self.check_shoot()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.balrog_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 25 
            self.game.enemyremain -=1
            print('boss balrog killed', self.game.enemyremain)

    def launchprojectilesboss(self):
        self.allprojectilesbossbalrog.add(ProjectilesBalrog(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilesbossbalrog.add(ProjectilesBalrog(self, self.game))        

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