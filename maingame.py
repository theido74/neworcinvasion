import pygame
from player import Player
from enemy import Enemy, Boss, EnemyOnBoat, BossBoat, EnemyWarg, BossWarg, EnemyDwarf, BossDwarf, EnemyGobelinArcher, EnemyGobelinMassue, BossBalrog, Peon
from sound import Sound
from bonus import BonusAttack,GoodElf, BonusMelee, GoodElfSword
from databaseconnection import DBConnection
from random import randint

class Game:
    def __init__(self):
        self.nameneed = False
        self.isplaying = False
        self.player = Player(self)
        self.goodelf = GoodElf(self)
        self.goodelfsword = GoodElfSword(self)
        self.bonusattack = BonusAttack(self)
        self.bonusmelee = BonusMelee(self)
        self.enemy = Enemy(self)
        self.peon = Peon(self)
        self.enemyonaboat = EnemyOnBoat(self)
        self.warg = EnemyWarg(self)
        self.dwarf = EnemyDwarf(self)
        self.gobelinarcher = EnemyGobelinArcher(self)
        self.gobelinmassue = EnemyGobelinMassue(self) 
        self.boss = Boss(self)
        self.bossboat = BossBoat(self)
        self.bosswarg = BossWarg(self)
        self.bossdwarf = BossDwarf(self)
        self.bossbalrog = BossBalrog(self)
        self.allboss = pygame.sprite.Group()
        self.allplayers = pygame.sprite.Group()
        self.allplayers.add(self.player)
        self.pressed = {}
        self.allgoodelf = pygame.sprite.Group()
        self.allgoodelfsword = pygame.sprite.Group()
        self.allbonusattack = pygame.sprite.Group()
        self.allbonusmelee = pygame.sprite.Group()
        self.allenemies = pygame.sprite.Group()
        self.allpeon = pygame.sprite.Group()
        self.allenemiesonaboat = pygame.sprite.Group()
        self.allwarg = pygame.sprite.Group()
        self.alldwarf = pygame.sprite.Group()
        self.allgobelinarcher = pygame.sprite.Group()
        self.allgobelinmassue = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()
        self.allprojectilesenemy = pygame.sprite.Group()
        self.allprojectilesenemyonaboat = pygame.sprite.Group()
        self.allprojectileswargpoison = pygame.sprite.Group()
        self.allprojectilesdwarf = pygame.sprite.Group()
        self.allprojectilesgobelinarcher = pygame.sprite.Group()
        self.allprojectilesgobelinmassue = pygame.sprite.Group()
        self.allprojectilesboss = pygame.sprite.Group()
        self.allprojectilesbossboat = pygame.sprite.Group()
        self.allprojectilesbosswarg = pygame.sprite.Group()
        self.allprojectilesbossdwarf = pygame.sprite.Group()
        self.allprojectilesbossbalrog = pygame.sprite.Group()
        self.allexploses = pygame.sprite.Group()
        self.score = 0
        self.music = Sound()
        self.bossspawned = False
        self.firstspawn = False
        self.secondspawn = False
        self.bonusattackspawn = False
        self.goodelfspawn = False
        self.enemyremain = 0
        self.bonusremain = 0
        self.db = DBConnection()
        self.userdata = self.db.finduserdic()


    def start(self):
        self.player.allprojectiles.empty()
        self.isplaying = True 
        self.firstspawn = True
        for _ in range(randint(1, 3)):   
            self.spawnenemy()
        for _ in range(randint(2, 4)):   
            self.spawnpeon()

    def startsecondspawn(self):
        self.player.allprojectiles.empty()
        self.isplaying = True
        self.secondspawn = True
        self.secondspawn = True
        for _ in range(randint(2,5)):
            self.spawnenemy()
        for _ in range(randint(3,6)):
            self.spawnpeon()
            
    def startlvl1(self):
        self.player.allprojectiles.empty()
        self.isplaying = True 
        self.firstspawn = True
        for _ in range(randint(4,6)):   
            self.spawnenemyboat()

    def startlvl1second(self):
        self.player.allprojectiles.empty()
        self.isplaying = True 
        self.secondspawn = True
        for _ in range(randint(6,7)):   
            self.spawnenemyboat()
        for _ in range(randint(2,5)):   
            self.spawnenemy()
        self.spawnbonusmelee()

    def startlvl2(self):
        self.player.allprojectiles.empty()
        self.isplaying = True
        self.firstspawn = True
        for _ in range(randint(6,7)):
            self.spawnwarg()
        if self.bonusattackspawn == False:
            for _ in range(1):
                self.spawnbonusattack()

    def startlvl2second(self):
        self.player.allprojectiles.empty()
        self.goodelf.allprojectilesgoodelf.empty()
        self.isplaying = True 
        self.secondspawn = True
        for _ in range(randint(8,10)):   
            self.spawnwarg()

    def startlvl3(self):
        self.bosswarg.allprojectilesbosswarg.empty()
        self.player.allprojectiles.empty()
        self.isplaying = True
        self.firstspawn = True
        for _ in range(randint(6,10)):
            self.spawndawrf()
        
    def startlvl3second(self):
        self.player.allprojectiles.empty()
        self.dwarf.allprojectiledwarf.empty()
        self.isplaying = True
        self.secondspawn = True
        for _ in range(randint(5,6)):   
            self.spawnenemy()
            print(self.enemyremain)
        for _ in range(randint(2,4)):
            self.spawndawrf()
            print(self.enemyremain)

    def startlvl4(self):
        self.player.allprojectiles.empty()
        self.isplaying = True
        self.firstspawn = True
        for _ in range(5):
            self.spwangobelinarcher()
            print(self.enemyremain)
        for _ in range(5):
            self.spwangobelinmassue()
            print(self.enemyremain)

    def startlvl4second(self):
        self.player.allprojectiles.empty()
        self.isplaying = True
        self.secondspawn = True        
        for _ in range(randint(7,8)):
            self.spwangobelinarcher()
        for _ in range(randint(12,20)):
            self.spwangobelinmassue()
            print(self.enemyremain)
    


    def startboss(self):
        self.player.allprojectiles.empty()
        if self.enemyremain == 0:
            self.spawnboss()
            self.bossspawned = True
            for _ in range(randint(3,4)):
                self.spawnpeon()
                self.spawnenemy()

    def startbossboat(self):
        self.player.allprojectiles.empty()
        self.spawnbonusattack()
        if self.enemyremain == 0:
            self.spawnbossboat()
            self.bossspawned = True
            for _ in range(randint(2,5)):
                self.spawnenemyboat()
                self.spawnenemyboat()

    def startbosswarg(self):
        self.player.allprojectiles.empty()
        self.spawnbonusattack()
        if self.enemyremain == 0:
            self.spawnbosswarg()
            self.bossspawned = True

    def startbossdwarf(self):
        self.player.allprojectiles.empty()
        if self.enemyremain == 0:
            for _ in range(2):
                self.spawnbossdwarf()
                self.bossspawned = True

    def startbossbalrog(self):
        self.player.allprojectiles.empty()
        if self.enemyremain == 0:
            self.spawnbossbalrog()
            self.bossspawned = True

    def nextlevel(self):
        self.bossspawned = False
        self.secondspawn = False
        self.player.maxhealth = self.player.maxhealth*1.4
        self.player.attack = self.player.attack*1.4
        self.player.health = self.player.maxhealth
        self.enemyremain = 0
        self.allprojectiles.remove()

    def gameover (self):
        if 'username' in self.userdata:
            username_value = self.userdata['username']
            self.db.savehighscore(username_value, self.score)

        self.level_number = 0
        self.score = 0
        self.allenemies = pygame.sprite.Group()
        self.player.health = self.player.maxhealth
        self.isplaying = False
        self.bossspawned = False
        self.firstspawn = False
        self.secondspawn = False

    def updatescore(self, screen):
        if 'highscore' in self.userdata:
            highscore_value = self.userdata['highscore']
            font = pygame.font.SysFont('Small font', 20, 0)
            nl = '\n'
            scoretext = font.render(f"Score: {self.score}{nl}Highscore: {highscore_value}", 1, (255, 0, 0))
            screen.blit(scoretext, (20,20))
            screen.blit(self.player.image, self.player.rect)
        else:
            font = pygame.font.SysFont('Small font', 20, 0)
            scoretext = font.render(f'Score : {self.score}', 1, (255,0,0))
            screen.blit(scoretext, (20,20))
            screen.blit(self.player.image, self.player.rect)
            
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
        
        self.allbonusattack.draw(screen)
        self.allbonusmelee.draw(screen)
        
        for goodelf in self.allgoodelf:
            goodelf.move()
            goodelf.updatehealthbar(screen)
            for projectile in self.goodelf.allprojectilesgoodelf:
                projectile.move()
                if self.goodelf.health <= 0:
                    self.allgoodelf.remove(self.goodelf)
            self.goodelf.allprojectilesgoodelf.draw(screen)
            self.allgoodelf.draw(screen)

        for goodelfsword in self.allgoodelfsword:
            goodelfsword.move()
            goodelfsword.updatehealthbar(screen)
        self.allgoodelfsword.draw(screen)

        for enemy in self.allenemies:
            enemy.move()
            enemy.updatehealthbar(screen)
            for projectile in enemy.allprojectilesenemy:
                projectile.update()
                projectile.move()
            enemy.allprojectilesenemy.draw(screen)
            self.allenemies.draw(screen)
                
        for boss in self.allboss:
            boss.move()
            boss.updatehealthbar(screen)
            for projectile in self.boss.allprojectilesboss:
                projectile.update()
                projectile.move()
                self.boss.allprojectilesboss.draw(screen)
                self.allboss.draw(screen)

        for peon in self.allpeon:
            peon.move()
            peon.updatehealthbar(screen)
        self.allpeon.draw(screen)

        for enemyonaboat in self.allenemiesonaboat:
            enemyonaboat.move()
            enemyonaboat.updatehealthbar(screen)
            for projectile in enemyonaboat.allprojectilesenemyonaboat:
                projectile.update()
                projectile.move()
            enemyonaboat.allprojectilesenemyonaboat.draw(screen)
            self.allenemiesonaboat.draw(screen)

        for bossboat in self.allboss:
            bossboat.move()
            bossboat.updatehealthbar(screen)
        self.allboss.draw(screen)

        for projectile in self.bossboat.allprojectilesbossboat:
            projectile.move()
        self.bossboat.allprojectilesbossboat.draw(screen)

        for warg in self.allwarg:
            warg.move()
            warg.updatehealthbar(screen)
            for projectile in warg.allprojectileswargpoison:
                projectile.move()
            warg.allprojectileswargpoison.draw(screen)
            self.allwarg.draw(screen)

        for bosswarg in self.allboss:
            bosswarg.move()
            bosswarg.updatehealthbar(screen)
        self.allboss.draw(screen)

        for projectile in self.bosswarg.allprojectilesbosswarg:
            projectile.move()
        self.bosswarg.allprojectilesbosswarg.draw(screen)

        for dwarf in self.alldwarf:
            dwarf.move()
            dwarf.updatehealthbar(screen)
            for projectile in dwarf.allprojectiledwarf:
                projectile.move()
            dwarf.allprojectiledwarf.draw(screen)
            self.alldwarf.draw(screen)

        for bossdwarf in self.allboss:
            bossdwarf.move()
            bossdwarf.updatehealthbar(screen)
        self.allboss.draw(screen)

        for projectile in self.bossdwarf.allprojectilesbossdwarf:
            projectile.move()
        self.bossdwarf.allprojectilesbossdwarf.draw(screen)

        for gobelinarcher in self.allgobelinarcher:
            gobelinarcher.move()
            gobelinarcher.updatehealthbar(screen)
        self.allgobelinarcher.draw(screen)

        for projectile in self.gobelinarcher.allprojectilesgobelinarcher:
            projectile.move()
        self.gobelinarcher.allprojectilesgobelinarcher.draw(screen)

        for gobelinmassue in self.allgobelinmassue:
            gobelinmassue.move()
            gobelinmassue.updatehealthbar(screen)
        self.allgobelinmassue.draw(screen)

        for projectile in self.gobelinmassue.allprojectilesgobelinmassue:
            projectile.move()
        self.gobelinmassue.allprojectilesgobelinmassue.draw(screen)

        for bossbalrog in self.allboss:
            bossbalrog.move()
            bossbalrog.updatehealthbar(screen)
        self.allboss.draw(screen)

        for projectile in self.bossbalrog.allprojectilesbossbalrog:
            projectile.move()
        self.bossbalrog.allprojectilesbossbalrog.draw(screen)

        for projectile in self.player.allprojectiles:
            self.player.allprojectiles.update()

        pygame.display.flip()

    
    def spawnbonusattack(self):
        self.bonusattack in self.allbonusattack
        self.bonusattack = BonusAttack(self)
        self.allbonusattack.add(self.bonusattack)
        self.bonusremain += 1
        self.bonusattackspawn = True

    def spawngoodelf(self):
        self.goodelf in self.allgoodelf
        self.goodelf = GoodElf(self)
        self.allgoodelf.add(self.goodelf)
        self.bonusremain += 1
        self.goodelfspawn = True

    def spawnbonusmelee(self):
        self.bonusmelee in self.allbonusmelee
        self.bonusmelee = BonusMelee(self)
        self.allbonusattack.add(self.bonusmelee)
        self.bonusremain += 1
        self.bonusattackspawn = True

    def spawngoodelfsword(self):
        self.goodelfsword in self.allgoodelfsword
        self.goodelfsword = GoodElfSword(self)
        self.allgoodelfsword.add(self.goodelfsword)
        self.bonusremain += 1
        self.goodelfspawn = True    

    def spawnenemy(self):
        self.enemy in self.allenemies
        self.enemy = Enemy(self)
        self.allenemies.add(self.enemy)
        self.enemyremain += 1

    def spawnpeon(self):
        self.enemy in self.allpeon
        self.peon = Peon(self)
        self.allpeon.add(self.peon)
        self.enemyremain += 1

    def spawnenemyboat(self):
        self.enemyonaboat in self.allenemiesonaboat
        self.enemyonaboat = EnemyOnBoat(self)
        self.allenemiesonaboat.add(self.enemyonaboat)
        self.enemyremain += 1

    def spawnwarg(self):
        self.warg in self.allwarg
        self.warg = EnemyWarg(self)
        self.allwarg.add(self.warg)
        self.enemyremain +=1

    def spawndawrf(self):
        self.dwarf in self.alldwarf
        self.dwarf = EnemyDwarf(self)
        self.alldwarf.add(self.dwarf)
        self.enemyremain +=1

    def spwangobelinarcher(self):
        self.gobelinarcher in self.allgobelinarcher
        self.gobelinarcher = EnemyGobelinArcher(self)
        self.allgobelinarcher.add(self.gobelinarcher)
        self.enemyremain +=1

    def spwangobelinmassue(self):
        self.gobelinmassue in self.allgobelinmassue
        self.gobelinmassue = EnemyGobelinMassue(self)
        self.allgobelinmassue.add(self.gobelinmassue)
        self.enemyremain +=1

    def spawnboss(self):
        self.boss = Boss(self)
        self.allboss.add(self.boss)
        self.enemyremain += 1
        self.bossspawned = True
    
    def spawnbossboat(self):
        self.bossboat = BossBoat(self)
        self.allboss.add(self.bossboat)
        self.enemyremain += 1
        self.bossspawned = True
    
    def spawnbosswarg(self):
        self.bosswarg = BossWarg(self)
        self.allboss.add(self.bosswarg)
        self.enemyremain += 1
        self.bossspawned = True
    
    def spawnbossdwarf(self):
        self.bossdwarf = BossDwarf(self)
        self.allboss.add(self.bossdwarf)
        self.enemyremain += 1
        self.bossspawned = True

    def spawnbossbalrog(self):
        self.bossbalrog = BossBalrog(self)
        self.allboss.add(self.bossbalrog)
        self.enemyremain += 1
        self.bossspawned = True



    
                


