import pygame
from pygame.math import Vector2
from random import randint
from projectiles import ProjectilesEnemy, ProjectilesBoss, ProjectilesEnemyOnaBoat, ProjectilesBossBoat, ProjectilesWargPoison, ProjectilesBossWarg,ProjectilesDwarf, ProjectilesBossDwarf,ProjectilesGobelinArcher, ProjectilesGobelinMassue, ProjectilesBalrog
from explose import Explose

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.velocity = 1.3
        self.image = pygame.image.load(r'image\orcenemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 460-self.rect.width)
        self.rect.y = 1
        self.position_x = randint(0, (450))
        self.position_y = randint(0, 301)
        self.projectileenemy = ProjectilesEnemy(self, game)
        self.allprojectilesenemy = pygame.sprite.Group()
        self.game = game
        self.health = 60
        self.maxhealth = self.health
        self.attack = 9
        self.shoot_cooldown = 1050
        self.last_shot_time = 0 
        self.boss = Boss

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 300)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time 

    def shoot(self):
        self.allprojectilesenemy.add(ProjectilesEnemy(self, self.game))    

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
            self.game.music.explose_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            self.kill()
            self.remove()
            self.game.score += 15
            self.game.enemyremain -=1

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
        self.health = 90 
        self.maxhealth = self.health
        self.attack = 4
        self.shoot_cooldown = 1300  
        self.last_shot_time = 0  

    def move(self):
        distance_to_player = pygame.math.Vector2(self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y).length()
        if distance_to_player < 50: 
            self.hit()
        player_position = Vector2(self.game.player.rect.x + 1, self.game.player.rect.y + 1)
        peon_position = Vector2(self.rect.x + 1, self.rect.y + 1)

        if player_position != peon_position:
            direction = (player_position - peon_position).normalize()
        else:
            direction = Vector2(0, 0)  

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
            self.kill()
            self.remove()
            self.game.score += 10
            self.game.enemyremain -=1

class EnemyOnBoat(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 1
        self.image = pygame.image.load(r'image\orconaaboat.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400- self.rect.width)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 300)
        self.projectileenemyonaboat = ProjectilesEnemyOnaBoat(self, game)
        self.allprojectilesenemyonaboat = pygame.sprite.Group()
        self.allenemiesonaboat = pygame.sprite.Group()
        self.game = game
        self.health = 400 
        self.maxhealth = self.health
        self.attack = 10
        self.shoot_cooldown = 2000  
        self.last_shot_time = 0 

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width/2))
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 550)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

    def shoot(self):
        self.allprojectilesenemyonaboat.add(ProjectilesEnemyOnaBoat(self, self.game))        
    
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
            self.game.music.boat_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            self.kill()
            self.game.score += 20
            self.game.enemyremain -=1

    def remove(self):
        self.game.remove(self)

class EnemyWarg(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 1.5
        self.image = pygame.image.load(r'image\wargenemy.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 400)
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 600)
        self.projectileswargpoison = ProjectilesWargPoison(self, game)
        self.allprojectileswargpoison = pygame.sprite.Group()
        self.allwarg = pygame.sprite.Group()
        self.game = game
        self.health = 500 
        self.maxhealth = self.health
        self.attack = 10
        self.shoot_cooldown = 2000  
        self.last_shot_time = 0 

    def move(self):
        player_hit = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in player_hit:
            player.damage(self.attack)
        goodelf_hit = pygame.sprite.spritecollide(self, self.game.allgoodelf, False)
        for goodelf in goodelf_hit:
            goodelf.damage(self.attack)
        goodelfsword_hit = pygame.sprite.spritecollide(self, self.game.allgoodelfsword, False)
        for goodelfsword in goodelfsword_hit:
            goodelfsword.damage(self.attack)

        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
        if self.rect.y < self.position_y:
            self.rect.y += self.velocity
        if self.rect.y > self.position_y:
            self.rect.y -= self.velocity
        if abs(self.rect.y - self.position_y) < self.velocity:
           self.position_y = randint(0, 600)
        self.check_shoot()

    def check_shoot(self):
        current_time = pygame.time.get_ticks()  
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

    def shoot(self):
        self.allprojectileswargpoison.add(ProjectilesWargPoison(self, self.game))        

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
            self.game.music.warg_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            self.kill()
            self.game.score += 25
            self.game.enemyremain -=1

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
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 300)
        self.projectiledwarf = ProjectilesDwarf(self, game)
        self.allprojectiledwarf = pygame.sprite.Group()
        self.alldwarf = pygame.sprite.Group()
        self.game = game
        self.health = 600 
        self.maxhealth = self.health
        self.attack = 4
        self.shoot_cooldown = 1800  
        self.last_shot_time = 0

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
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time 
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
            self.kill()
            self.game.score += 30
            self.game.enemyremain -=1

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
        self.health = 1000
        self.maxhealth = self.health
        self.attack = 20
        self.shoot_cooldown = 300 
        self.last_shot_time = 0 

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
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

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
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1

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
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 500)
        self.projectilegobelinmassue = ProjectilesGobelinMassue(self, game)
        self.allprojectilesgobelinmassue = pygame.sprite.Group()
        self.allgobelinmassue = pygame.sprite.Group()
        self.game = game
        self.health = 1000 
        self.maxhealth = self.health
        self.attack = 20
        self.shoot_cooldown = 1300  
        self.last_shot_time = 0

    def move(self):
        distance_to_player = pygame.math.Vector2(self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y).length()
        if distance_to_player < 50:
            self.hit()
        player_position = Vector2(self.game.player.rect.x + 1, self.game.player.rect.y + 1)
        peon_position = Vector2(self.rect.x + 1, self.rect.y + 1)

        if player_position != peon_position:
            direction = (player_position - peon_position).normalize()
        else:
            direction = Vector2(0, 0)  

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
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time  

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
            self.kill()
            self.game.score += 7
            self.game.enemyremain -=1

    def remove(self):
        self.game.remove(self)

class Boss(Enemy,pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load(r'image\orcboss.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (430))
        self.position_y = randint(0, 350)
        self.projectileboss = ProjectilesBoss(self, game)
        self.allprojectilesboss = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 600
        self.maxhealth = self.health
        self.attack = 13
        self.shoot_cooldown = 6000
        self.last_shot_time = 0

    def move(self):
        if abs(self.rect.x - self.position_x) > self.velocity/2:
            if self.rect.x < self.position_x:
                self.rect.x += self.velocity 
            elif self.rect.x > self.position_x:          
                self.rect.x -= self.velocity 

        if abs(self.rect.y - self.position_y) > self.velocity/2:
            if self.rect.y < self.position_y:
                self.rect.y += self.velocity 
            elif self.rect.y > self.position_y:
                self.rect.y -= self.velocity 

        if abs(self.rect.x - self.position_x) < self.velocity/2 and abs(self.rect.y - self.position_y) < self.velocity/2:
            self.position_x = randint(0, (460 - self.rect.width))
            self.position_y = randint(0, 350)
            self.launchprojectilesboss() 
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.explose_boss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            self.kill()
            self.remove()
            self.game.score += 50 
            self.game.enemyremain -=1

    def launchprojectilesboss(self):
        self.allprojectilesboss.add(ProjectilesBoss(self, self.game))

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
        self.health = 900
        self.maxhealth = self.health
        self.attack = 60
        self.shoot_cooldown = 6000 
        self.last_shot_time = 0 

    def move(self):
        if self.rect.y > 150:
            self.rect.y = 150
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
           self.launchprojectilesboss() 
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
        bar_width = int(min(self.health / self.maxhealth * self.rect.width, max_bar_width))
        bar_position = [self.rect.x + (self.rect.width - bar_width) // 2, self.rect.y + self.rect.height, bar_width, bar_height]
        bg_bar_position = [self.rect.x, self.rect.y + self.rect.height, self.rect.width, bar_height]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launchprojectilesboss(self):
        self.allprojectilesbossboat.add(ProjectilesBossBoat(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

    def shoot(self):
        self.allprojectilesbossboat.add(ProjectilesBossBoat(self, self.game))        

    def kill(self):
        super().kill()
        
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.music.boatboss_sound.play()
            self.game.allexploses.add(Explose(self.rect.x, self.rect.y))
            self.kill()
            self.remove()
            self.game.score += 75 
            self.game.enemyremain -=1

class BossWarg(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.6
        self.image = pygame.image.load(r'image\bossorcwarg.png')
        self.image = pygame.transform.scale(self.image, (140, 140))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 450)
        self.projectilebosswarg = ProjectilesBossWarg(self, game)
        self.allprojectilesbosswarg = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 2200
        self.maxhealth = self.health
        self.attack = 17
        self.shoot_cooldown = 3500 
        self.last_shot_time = 0 

    def move(self):
        player_hit = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in player_hit:
            player.damage(self.attack)
        goodelf_hit = pygame.sprite.spritecollide(self, self.game.allgoodelf, False)
        for goodelf in goodelf_hit:
            goodelf.damage(self.attack)
        goodelfsword_hit = pygame.sprite.spritecollide(self, self.game.allgoodelfsword, False)
        for goodelfsword in goodelfsword_hit:
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
            self.kill()
            self.game.score += 100 
            self.game.enemyremain -=1

    def launchprojectilesboss(self):
        self.allprojectilesbosswarg.add(ProjectilesBossWarg(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time
    def shoot(self):
        self.allprojectilesbosswarg.add(ProjectilesBossWarg(self, self.game))        

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



class BossDwarf(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.6
        self.image = pygame.image.load(r'image\bossnainenemy.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 300)
        self.projectilebossdwarf = ProjectilesBossDwarf(self, game)
        self.allprojectilesbossdwarf = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 3000
        self.maxhealth = self.health
        self.attack = 100
        self.shoot_cooldown = 4000  
        self.last_shot_time = 0

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
            self.kill()
            self.game.score += 150 
            self.game.enemyremain -=1

    def launchprojectilesboss(self):
        self.allprojectilesbossdwarf.add(ProjectilesBossDwarf(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time 

    def shoot(self):
        self.allprojectilesbossdwarf.add(ProjectilesBossDwarf(self, self.game))        

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

class BossBalrog(Enemy, pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.velocity = 0.7
        self.image = pygame.image.load(r'image\balrog.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 200- int(self.rect.width /2 )
        self.rect.y = 1
        self.position_x = randint(0, (460 - self.rect.width/2))
        self.position_y = randint(0, 300)
        self.projectilebossbalrog = ProjectilesBalrog(self, game)
        self.allprojectilesbossbalrog = pygame.sprite.Group()
        self.allboss = pygame.sprite.Group()
        self.game = game
        self.health = 10000
        self.maxhealth = self.health
        self.attack = 200
        self.shoot_cooldown = 5000  
        self.last_shot_time = 0 

    def move(self):
        if self.rect.x < self.position_x:
            self.rect.x += self.velocity
        if self.rect.x > self.position_x:          
            self.rect.x-= self.velocity
        if abs(self.rect.x - self.position_x) < self.velocity/2:
           self.position_x = randint(0, (460 - self.rect.width))
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
            self.kill()
            self.game.score += 25 
            self.game.enemyremain -=1

    def launchprojectilesboss(self):
        self.allprojectilesbossbalrog.add(ProjectilesBalrog(self, self.game))

    def check_shoot(self):
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time
    def shoot(self):
        self.allprojectilesbossbalrog.add(ProjectilesBalrog(self, self.game))        

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