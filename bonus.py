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
        self.health = 1
        self.maxhealth = self.health

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.bonusattack_sound.play()
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
        self.health = 1
        self.maxhealth = self.health

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.bonusattack_sound.play()
            self.kill()
            self.game.spawngoodelfsword()
            self.game.bonusremain -= 1
            self.game.bonusattackspawn = False

class GoodElf(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load(r'image\elfbonus.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 600
        self.position_x = randint(120, (350 - self.rect.width))
        self.position_y = randint(400, 550)
        self.projectilesgoodelf = ProjectilesGoodelf(self, game)
        self.allprojectilesgoodelf = pygame.sprite.Group()
        self.game = game
        self.health = 500
        self.maxhealth = self.health
        self.attack = 5
        self.shoot_cooldown = 1000 
        self.last_shot_time = 0 

    def move(self):

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
           self.position_y = randint(400, 550)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time 

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
            self.kill()
            self.remove()
            self.game.score -= 15
            self.game.bonusremain -=1
       

class GoodElfSword(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load(r'image\goodelfsword.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
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
            enemy.damage(self.attack)

        peon_hit = pygame.sprite.spritecollide(self, self.game.allpeon, False)
        for enemy in peon_hit:
            enemy.damage(self.attack)

        enemies_boat_hit= pygame.sprite.spritecollide(self, self.game.allenemiesonaboat, False)
        for enemy in enemies_boat_hit:
            enemy.damage(self.attack)

        warg_hit=pygame.sprite.spritecollide(self, self.game.allwarg, False)
        for enemy in warg_hit:
            enemy.damage(self.attack)
        
        dwarf_hit=pygame.sprite.spritecollide(self, self.game.alldwarf, False)
        for enemy in dwarf_hit:
            enemy.damage(self.attack)

        gobelinarcher_hit=pygame.sprite.spritecollide(self, self.game.allgobelinarcher, False)
        for enemy in gobelinarcher_hit:
            enemy.damage(self.attack)

        gobelinmassue_hit=pygame.sprite.spritecollide(self, self.game.allgobelinmassue, False)
        for enemy in gobelinmassue_hit:
            enemy.damage(self.attack)


        boss_hit = pygame.sprite.spritecollide(self, self.game.allboss, False)
        for boss in boss_hit:
            boss.damage(self.attack)

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
            self.kill()
            self.remove()
            self.game.score -= 15
            self.game.bonusremain -=1
       
