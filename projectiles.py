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

        enemies_boat_hit= pygame.sprite.spritecollide(self, self.game.allenemiesonaboat, False)
        for enemy in enemies_boat_hit:
            # Réduisez la vie de l'ennemi en fonction de l'attaque du joueur
            enemy.damage(self.player.attack)


        self.game.player.allprojectiles.add(self)

        boss_hit = pygame.sprite.spritecollide(self, self.game.allboss, False)
        for boss in boss_hit:
            # Réduisez la vie du boss en fonction de l'attaque du joueur
            boss.damage(self.player.attack)


        self.game.player.allprojectiles.add(self)
       

    def remove(self):
        self.game.allprojectiles.remove(self)

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

    def remove(self):
        self.game.allprojectilesenemy.remove(self)


class ProjectilesEnemyOnaBoat(ProjectilesEnemy):
    def __init__(self, enemyonaboat, game):
        super().__init__(enemyonaboat, game)
        self.velocity = 10
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\filetorc.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
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



class ProjectilesBoss (ProjectilesEnemy):
    def __init__(self, boss, game):
        super().__init__(boss, game)
        self.velocity = 7
        self.image = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\energiebossorc.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 150))
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
