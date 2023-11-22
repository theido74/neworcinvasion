import pygame
from maingame import Game
from text import show_text_window, wait_for_key_press
from databaseconnection import DBConnection
class Level:
    
    def __init__(self, level_number, background_path):
        self.level_number = level_number
        self.background = pygame.image.load(background_path).convert_alpha()
        self.banner = pygame.image.load(r'image\presstoplay.png').convert_alpha()
        self.game = Game()
        self.db = DBConnection()
        self.y_background = 0
        self.running = True
        self.showing_message = False

  
    def run_level(self, screen, clock):
        level_completed = False
        while self.running: 
            screen.fill((0, 0, 0))  # Effacer l'écran

            self.y_background += 0.7
            x_background = int(-0.18 * self.game.player.rect.x)
            if self.y_background < 728: 
                screen.blit(self.background, (x_background, int(self.y_background)))  # Arrière-plan
                screen.blit(self.background, (x_background, int(self.y_background - 728)))
            else:
                self.y_background = 0
                screen.blit(self.background, (x_background, int(self.y_background)))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN: 
                    self.game.pressed[event.key] = True

                    if event.key == pygame.K_SPACE:
                        self.game.player.launchprojectile()

                    if event.key == pygame.K_s :
                        self.game.start()
                        self.level_number = 0
                         

                elif event.type == pygame.KEYUP:
                    self.game.pressed[event.key] = False
        

            if self.game.isplaying:
                self.game.updatescore(screen)

            else:
                screen.blit(self.banner, (50, 150))
                pygame.display.flip()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game .secondspawn == False and self.level_number == 0:
                self.game.startsecondspawn()                
                self.game.player.allprojectiles.empty()


            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 0:
                self.game.startboss()
   
                self.game.player.allprojectiles.empty()
                self.game.enemy.allprojectilesenemy.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 0:
                self.level_number +=1
                level_completed = True       
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.boss.allprojectilesboss.empty()
                print('level',self.level_number)
            
            if self.level_number == 1:
                self.background = pygame.image.load(r'image\fondlvl1.jpg').convert_alpha()
                level_completed = False
 
            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 1:          
                self.game.startlvl1()
                print('startboat1')
                self.game.allprojectiles.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 1:
                self.game.startlvl1second()

                self.game.allprojectiles.empty()
                self.game.allprojectilesenemyonaboat.empty()
                print('start boat 2nd')

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 1:
                self.game.startbossboat()
                self.game.enemyonaboat.allprojectilesenemyonaboat.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 1:
                self.level_number +=1
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                self.game.bossboat.allprojectilesbossboat.empty()
                print('level',self.level_number)

            
            if self.level_number == 2:
                self.background = pygame.image.load(r'image\fondlvl2.png').convert_alpha()
                level_completed = False

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 2:          
                self.game.startlvl2()
                print('startwarg1')

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 2:
                self.game.startlvl2second()
                self.game.player.allprojectiles.empty()
                self.game.warg.allprojectileswargpoison.empty()
            
            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 2:
                self.game.startbosswarg()
                self.game.warg.allprojectileswargpoison.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 2:
                self.level_number +=1
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                print('level',self.level_number)

            if self.level_number == 3:
                self.background = pygame.image.load(r'image\fondlvl3.png').convert_alpha()
                level_completed = False

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 3:          
                self.game.startlvl3()
                print('startdwarf1')

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 3:
                self.game.startlvl3second()
                self.game.player.allprojectiles.empty()
                self.game.warg.allprojectileswargpoison.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 3:
                self.game.startbossdwarf()
                self.game.warg.allprojectileswargpoison.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 3:
                self.level_number +=1
                level_completed = True   
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                print('level',self.level_number)
                self.game.bossdwarf.allprojectilesbossdwarf.empty()
                self.game.player.allprojectiles.empty()

            if self.level_number == 4:
                self.background = pygame.image.load(r'image\fondlvl4.png').convert_alpha()
                level_completed = False


            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 4:          
                self.game.startlvl4()
                print('startgobelin1')

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 4:
                self.game.startlvl4second()
                self.game.player.allprojectiles.empty()
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty()  

            if self.game.isplaying and self.game.bossspawned == False and self.game.enemyremain == 0 and not level_completed and self.level_number == 4:
                self.level_number +=1 
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                print('level',self.level_number)
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty() 

            if self.level_number == 5:
                self.background = pygame.image.load(r'image\fondlvl5.png').convert_alpha()
                level_completed = False  

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 5:          
                self.game.startbossbalrog()
                print('startbalrog')
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty()  

            

            if self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x + self.game.player.rect.width < screen.get_width():
                self.game.player.move_right()
            if self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x > 0:
                self.game.player.move_left()
            if self.game.pressed.get(pygame.K_DOWN) and self.game.player.rect.y + self.game.player.rect.height < screen.get_height():
                self.game.player.move_up()
            if self.game.pressed.get(pygame.K_UP) and self.game.player.rect.y > 0:
                self.game.player.move_down()

            clock.tick(60)

def run_game():
# Initialisation de Pygame
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Space Orc Invasion')
    screen = pygame.display.set_mode((432, 680))

    # Création des niveaux
    level_0 = Level(0, r'image\fond1.png')


    # Boucle principale du jeu
    running = True
    while running:
        level_0.run_level(screen, clock)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False

        pygame.display.update()

    pygame.quit()

run_game()

