import pygame


class Projectiles(pygame.sprite.Sprite):
    def __init__(self, player, game):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\boulenergie copie.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.player = player
        self.game = game
        self.rect.x = player.rect.x + 10
        self.rect.y = player.rect.y

    def move(self):
        self.rect.y -= self.velocity
        if self.rect.y <= 0 - self.image.get_height():
            self.remove()
        enemies_hit = pygame.sprite.spritecollide(self, self.game.allenemies, False)
        for enemy in enemies_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        peon_hit = pygame.sprite.spritecollide(self, self.game.allpeon, False)
        for enemy in peon_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        enemies_boat_hit= pygame.sprite.spritecollide(self, self.game.allenemiesonaboat, False)
        for enemy in enemies_boat_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        warg_hit=pygame.sprite.spritecollide(self, self.game.allwarg, False)
        for enemy in warg_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)
        
        dwarf_hit=pygame.sprite.spritecollide(self, self.game.alldwarf, False)
        for enemy in dwarf_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        gobelinarcher_hit=pygame.sprite.spritecollide(self, self.game.allgobelinarcher, False)
        for enemy in gobelinarcher_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        gobelinmassue_hit=pygame.sprite.spritecollide(self, self.game.allgobelinmassue, False)
        for enemy in gobelinmassue_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)

        self.game.player.allprojectiles.add(self)

        boss_hit = pygame.sprite.spritecollide(self, self.game.allboss, False)
        for boss in boss_hit:
            # Réduisez la vie du boss en fonction de l'attaque du joueur
            boss.damage(self.player.attack)

        self.game.player.allprojectiles.add(self)
       

    def remove(self):
        self.game.player.allprojectiles.remove(self)

class ProjectilesGoodelf(pygame.sprite.Sprite):
    def __init__(self, bonus, game):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load(r'c:\Users\ponce\Desktop\python\23.10.23.space\Image\game\flecheelf.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.bonus = bonus
        self.game = game
        self.rect.x = bonus.rect.x + 10
        self.rect.y = bonus.rect.y

    def move(self):
        self.rect.y -= self.velocity
        if self.rect.y <= 0 - self.image.get_height():
            self.remove()
        enemies_hit = pygame.sprite.spritecollide(self, self.game.allenemies, False)
        for enemy in enemies_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)

        peon_hit = pygame.sprite.spritecollide(self, self.game.allpeon, False)
        for enemy in peon_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)

        enemies_boat_hit= pygame.sprite.spritecollide(self, self.game.allenemiesonaboat, False)
        for enemy in enemies_boat_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)

        warg_hit=pygame.sprite.spritecollide(self, self.game.allwarg, False)
        for enemy in warg_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)
        
        dwarf_hit=pygame.sprite.spritecollide(self, self.game.alldwarf, False)
        for enemy in dwarf_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)

        gobelinarcher_hit=pygame.sprite.spritecollide(self, self.game.allgobelinarcher, False)
        for enemy in gobelinarcher_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)

        gobelinmassue_hit=pygame.sprite.spritecollide(self, self.game.allgobelinmassue, False)
        for enemy in gobelinmassue_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.bonus.attack)


        boss_hit = pygame.sprite.spritecollide(self, self.game.allboss, False)
        for boss in boss_hit:
            # Réduisez la vie du boss en fonction de l'attaque du joueur
            boss.damage(self.bonus.attack)

       

    def remove(self):
        self.game.goodelf.allprojectilesgoodelf.remove(self)

class ProjectilesEnemy(pygame.sprite.Sprite):
    def __init__(self, enemy, game):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\Blind chess openning\Image\game\laserenemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.enemy = enemy
        self.game = game
        self.rect.x = enemy.rect.x - 20
        self.rect.y = enemy.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.enemy.attack)

        self.game.enemy.allprojectilesenemy.add(self)

        hitsbonus = pygame.sprite.spritecollide(self, self.game.allgoodelf, False)
        for goodelf in hitsbonus:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            goodelf.damage(self.enemy.attack)

        self.game.enemy.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)


class ProjectilesEnemyOnaBoat(ProjectilesEnemy):
    def __init__(self, enemyonaboat, game):
        super().__init__(enemyonaboat, game)
        self.velocity = 8
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\filetorc.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.enemyonaboat = enemyonaboat
        self.game = game
        self.rect.x = enemyonaboat.rect.x - 20
        self.rect.y = enemyonaboat.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.enemyonaboat.attack)

        self.game.enemyonaboat.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)



class ProjectilesWargPoison(ProjectilesEnemy):
    def __init__(self, warg, game):
        super().__init__(warg, game)
        self.velocity = 9
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\wargpoison.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.warg = warg
        self.game = game
        self.rect.x = warg.rect.x - 20
        self.rect.y = warg.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.warg.attack)

        self.game.warg.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)


class ProjectilesDwarf(ProjectilesEnemy):
    def __init__(self, dwarf, game):
        super().__init__(dwarf, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\hachenain.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.dwarf = dwarf
        self.game = game
        self.rect.x = dwarf.rect.x - 20
        self.rect.y = dwarf.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.dwarf.attack)

        self.game.dwarf.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)

class ProjectilesGobelinArcher(ProjectilesEnemy):
    def __init__(self, gobelinarcher, game):
        super().__init__(gobelinarcher, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\lasergobelin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.gobelinarcher = gobelinarcher
        self.game = game
        self.rect.x = gobelinarcher.rect.x - 20
        self.rect.y = gobelinarcher.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.gobelinarcher.attack)

        self.game.gobelinarcher.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)


class ProjectilesGobelinMassue(ProjectilesEnemy):
    def __init__(self, gobelinmassue, game):
        super().__init__(gobelinmassue, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\massuegobelin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.gobelinmassue = gobelinmassue
        self.game = game
        self.rect.x = gobelinmassue.rect.x - 20
        self.rect.y = gobelinmassue.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.gobelinmassue.attack)

        self.game.gobelinmassue.allprojectilesenemy.add(self)

    def remove(self):
        self.game.allprojectilesenemy.remove(self)


class ProjectilesBoss (ProjectilesEnemy):
    def __init__(self, boss, game):
        super().__init__(boss, game)
        self.velocity = 7
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\energiebossorc.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 150))
        self.rect = self.image.get_rect()
        self.boss = boss
        self.game = game
        self.rect.x = boss.rect.x - 20
        self.rect.y = boss.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.boss.attack)

        self.game.boss.allprojectilesboss.add(self)

    def remove(self):
        self.game.allprojectilesboss.remove(self)

class ProjectilesBossBoat (ProjectilesEnemy):
    def __init__(self, bossboat, game):
        super().__init__(bossboat, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\boulet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.bossboat = bossboat
        self.game = game
        self.rect.x = bossboat.rect.x - 20
        self.rect.y = bossboat.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.bossboat.attack)

        self.game.bossboat.allprojectilesbossboat.add(self)

    def remove(self):
        self.game.allprojectilesbossboat.remove(self)


class ProjectilesBossWarg (ProjectilesEnemy):
    def __init__(self, bosswarg, game):
        super().__init__(bosswarg, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\hachebosswarg.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image = pygame.transform.flip(self.image,False,True)
        self.rect = self.image.get_rect()
        self.bosswarg = bosswarg
        self.game = game
        self.rect.x = bosswarg.rect.x - 20
        self.rect.y = bosswarg.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.bosswarg.attack)

        self.game.bosswarg.allprojectilesbosswarg.add(self)

    def remove(self):
        self.game.allprojectilesbosswarg.remove(self)


class ProjectilesBossDwarf (ProjectilesEnemy):
    def __init__(self, bossdwarf, game):
        super().__init__(bossdwarf, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\hachebossnain.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.bossdwarf = bossdwarf
        self.game = game
        self.rect.x = bossdwarf.rect.x - 20
        self.rect.y = bossdwarf.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.bossdwarf.attack)

        self.game.bossdwarf.allprojectilesbossdwarf.add(self)

    def remove(self):
        self.game.allprojectilesbossdwarf.remove(self)

class ProjectilesBalrog (ProjectilesEnemy):
    def __init__(self, balrog, game):
        super().__init__(balrog, game)
        self.velocity = 3
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\fouetbalrog.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.balrog = balrog
        self.game = game
        self.rect.x = balrog.rect.x - 35
        self.rect.y = balrog.rect.y
        self.initipos_y = self.rect.y

    def move(self):
        self.rect.y += self.velocity
        if self.rect.y > 728: 
            self.remove()
        hits = pygame.sprite.spritecollide(self, self.game.allplayers, False)
        for player in hits:
            # Réduisez la vie du joueur en fonction de l'attaque de l'ennemi
            player.damage(self.balrog.attack)

        self.game.bossbalrog.allprojectilesbossbalrog.add(self)

    def remove(self):
        self.game.allprojectilesbossbalrog.remove(self)