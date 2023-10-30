import pygame
from player import Player
from enemy import Enemy, Boss, EnemyOnBoat
from sound import Sound


class Game:
    def __init__(self):
        self.nameneed = False
        self.isplaying = False
        self.player = Player(self)
        self.enemy = Enemy(self)
        self.enemyonaboat = EnemyOnBoat(self)
        self.boss = Boss(self)
        self.allboss = pygame.sprite.Group()
        self.allplayers = pygame.sprite.Group()
        self.allplayers.add(self.player)
        self.pressed = {}
        self.allenemies = pygame.sprite.Group()
        self.allenemiesonaboat = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()
        self.allprojectilesenemy = pygame.sprite.Group()
        self.allprojectilesenemyonaboat = pygame.sprite.Group()
        self.allprojectilesboss = pygame.sprite.Group()
        self.allexploses = pygame.sprite.Group()
        self.score = 0
        self.level = 0
        self.music = Sound()
        self.bossspawned = False

    def start(self):
        self.isplaying = True 
        for _ in range(5):   
            self.spawnenemy()
    
    def startlvl1(self):
        self.isplaying = True 
        for _ in range(5):   
            self.spawnenemyboat()
   
    
    def check_level_completion(self):
        if len(self.allenemies) == 0 and not self.bossspawned:
                self.spawnboss()
                self.bossspawned = True
                print('level', self.level)
                self.startlvl1()
        
    def gameover (self):
        self.level = 0
        self.score = 0
        self.allenemies = pygame.sprite.Group()
        self.player.health = self.player.maxhealth
        self.isplaying = False
        self.bossspawned = False

    def updatescore(self, screen):
        font = pygame.font.SysFont('Small font', 20, 0)
        scoretext = font.render(f'Score : {self.score}', 1, (255,0,0))
        screen.blit(scoretext, (20,20))
        screen.blit(self.player.image, self.player.rect)#position du joueur. rec sert a detecter la position du joueur voir terminal


        for explose in self.allexploses:
            if explose.animation:
                explose.animate()
            else:
                self.allexploses.remove(explose)
        self.allexploses.draw(screen)

        for projectile in self.player.allprojectiles:
            projectile.move()
        self.player.allprojectiles.draw(screen)

        for player in self.allplayers:
            self.player.updatehealthbar(screen)
            if player.health <= 0:
                self.isplaying = False

        for enemy in self.allenemies:
            enemy.move()
            enemy.updatehealthbar(screen)
        self.allenemies.draw(screen)

        for projectile in self.enemy.allprojectilesenemy:
            projectile.move()
            if self.enemy.health <= 0:
                self.allenemies.remove(self.enemy)
        self.enemy.allprojectilesenemy.draw(screen)
            

        for projectile in self.boss.allprojectilesboss:
            projectile.move()
        self.boss.allprojectilesboss.draw(screen)
                
        for enemy in self.allenemies:
            self.enemy.updatehealthbar(screen)
        
        for boss in self.allboss:
            boss.move()
            boss.updatehealthbar(screen)
        self.allboss.draw(screen)

        for enemyinboat in self.allenemiesonaboat:
            enemyinboat.move()
            enemyinboat.updatehealthbar(screen)
        self.allenemiesonaboat.draw(screen)

        for projectile in self.enemyonaboat.allprojectilesenemyonaboat:
            projectile.move()
        self.enemyonaboat.allprojectilesenemyonaboat.draw(screen)

        self.check_level_completion()
        pygame.display.flip()#maj ecran

    
    def spawnenemy(self):
        self.enemy in self.allenemies
        self.enemy = Enemy(self)
        self.allenemies.add(self.enemy)

    def spawnenemyboat(self):
        self.enemyonaboat in self.allenemiesonaboat
        self.enemyonaboat = EnemyOnBoat(self)
        self.allenemiesonaboat.add(self.enemyonaboat)

    def spawnboss(self):
        self.boss = Boss(self)
        self.allboss.add(self.boss)


