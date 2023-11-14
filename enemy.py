import pygame
from random import randint
from projectiles import ProjectilesEnemy, ProjectilesBoss, ProjectilesEnemyOnaBoat, ProjectilesBossBoat, ProjectilesWargPoison, ProjectilesBossWarg,ProjectilesDwarf, ProjectilesBossDwarf,ProjectilesGobelinArcher, ProjectilesGobelinMassue, ProjectilesBalrog
from explose import Explose

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\orc1.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileenemy = ProjectilesEnemy(self, game)
        self.allprojectilesenemy = pygame.sprite.Group()
        self.game = game
        self.health = 100 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.explose_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 15
            self.game.enemyremain -=1
            print(self.game.enemyremain)
       
    def remove(self):
        self.game.remove(self)

class EnemyOnBoat(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\orconaboat1-pixelicious.png')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileenemyonaboat = ProjectilesEnemyOnaBoat(self, game)
        self.allprojectilesenemyonaboat = pygame.sprite.Group()
        self.allenemiesonaboat = pygame.sprite.Group()
        self.game = game
        self.health = 100 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
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
        self.velocity = 4
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\warg.png')
        self.image = pygame.transform.scale(self.image, (120, 110))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilewargpoison = ProjectilesWargPoison(self, game)
        self.allprojectilewargpoison = pygame.sprite.Group()
        self.allwarg = pygame.sprite.Group()
        self.game = game
        self.health = 300 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
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
           self.position_y = randint(0, 550)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  # Obtenez le temps actuel en millisecondes
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

    def shoot(self):
        self.allprojectilewargpoison.add(ProjectilesWargPoison(self, self.game))        
    
    def launchprojectileswargpoison(self):
        self.allprojectilewargpoison.add(ProjectilesWargPoison(self, self.game))

    def kill(self):
        super().kill()

    def updatehealthbar(self, surface):
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.warg_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1
            print('warg killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyDwarf(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 4
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\nain avec hache.png')
        self.image = pygame.transform.scale(self.image, (120, 110))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectiledwarf = ProjectilesDwarf(self, game)
        self.allprojectiledwarf = pygame.sprite.Group()
        self.alldwarf = pygame.sprite.Group()
        self.game = game
        self.health = 300 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesdwarf() 
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
        self.allprojectiledwarf.add(ProjectilesDwarf(self, self.game))        
    
    def launchprojectilesdwarf(self):
        self.allprojectiledwarf.add(ProjectilesDwarf(self, self.game))

    def kill(self):
        super().kill()

    def updatehealthbar(self, surface):
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.dwarf_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1
            print('dwarf killed', self.game.enemyremain)

    def remove(self):
        self.game.remove(self)


class EnemyGobelinArcher(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 4
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\gobelinarcher.png')
        self.image = pygame.transform.scale(self.image, (120, 110))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilegobelinarcher = ProjectilesGobelinArcher(self, game)
        self.allprojectilegobelinarcher = pygame.sprite.Group()
        self.allgobelinarcher = pygame.sprite.Group()
        self.game = game
        self.health = 300 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesdwarf() 
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
        self.allprojectilegobelinarcher.add(ProjectilesGobelinArcher(self, self.game))        
    
    def launchprojectilesdwarf(self):
        self.allprojectilegobelinarcher.add(ProjectilesGobelinArcher(self, self.game))

    def kill(self):
        super().kill()

    def updatehealthbar(self, surface):
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
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
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\gobelinmassue.png')
        self.image = pygame.transform.scale(self.image, (120, 110))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilegobelinmassue = ProjectilesGobelinMassue(self, game)
        self.allprojectilegobelinmassue = pygame.sprite.Group()
        self.allgobelinmassue = pygame.sprite.Group()
        self.game = game
        self.health = 300 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 2
        self.shoot_cooldown = 1300  # Temps en millisecondes entre chaque tir
        self.last_shot_time = 0  # Temps du dernier tir

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesgobelinmassue() 
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
        self.allprojectilegobelinmassue.add(ProjectilesGobelinMassue(self, self.game))        
    
    def launchprojectilesgobelinmassue(self):
        self.allprojectilegobelinmassue.add(ProjectilesGobelinMassue(self, self.game))

    def kill(self):
        super().kill()

    def updatehealthbar(self, surface):
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)
    
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
        self.velocity = 1
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\orcboss.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectileboss = ProjectilesBoss(self, game)
        self.allprojectilesboss = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
        self.shoot_cooldown = 1000  # Temps en millisecondes entre chaque tir
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
            self.game.music.explose_boss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)


class BossBoat(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 2
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\Bigboatorc.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilebossboat = ProjectilesBossBoat(self, game)
        self.allprojectilesbossboat = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
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
            self.game.music.boatboss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            # L'ennemi est vaincu, vous pouvez prendre des mesures ici
            self.kill()
            self.game.score += 25 
            self.game.enemyremain -=1
            print('boss boat killed', self.game.enemyremain)

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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)



class BossWarg(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 2
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\orcwarg.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width))
        self.position_y = randint(0, 300)
        self.projectilebosswarg = ProjectilesBossWarg(self, game)
        self.allprojectilesbosswarg = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)



class BossDwarf(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 2
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\naincyborg avec hache.png')
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
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)

class BossBalrog(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 2
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\balrog.png')
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
        self.health = 350 # Nombre de vies initiales
        self.maxhealth = self.health
        self.attack = 1
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
        barcolor = (71, 209,71)
        bgbarcolor = (230, 0, 0)
        barposition = [self.rect.x + 5, self.rect.y -10, self.health, 5]
        bgbarposition = [self.rect.x + 5, self.rect.y - 10, self.maxhealth, 5]

        pygame.draw.rect(surface, bgbarcolor, bgbarposition)
        pygame.draw.rect(surface, barcolor, barposition)