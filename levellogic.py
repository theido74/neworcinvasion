import pygame
from maingame import Game
from text import show_text_window, wait_for_key_press, show_image , show_image_no_scale
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
                

                    if event.key == pygame.K_s and self.game.isplaying == False :
                        show_image_no_scale(screen,r'image\gandalfstory2 copie.png',0,0)
                        show_text_window(screen, "Press sur 'C' to continue")
                        wait_for_key_press(pygame.K_c)
                        show_image_no_scale(screen,r'image\gandalfstory2_2 copie.png',0,0)
                        show_text_window(screen, "Press sur 'C' to continue")
                        wait_for_key_press(pygame.K_c)
                        self.level_number = 0
                        self.game.isplaying = True
                        self.background = pygame.image.load(r'image\fond1.png').convert_alpha()
                        self.game.start()


                elif event.type == pygame.KEYUP:
                    self.game.pressed[event.key] = False
                            
            self.game.player.allprojectiles.update(screen)

            if self.game.isplaying == False and self.game.gameover:
                self.game.allenemies.empty()
                self.game.allpeon.empty()
                self.game.allbonusattack.empty()
                self.game.allbonusmelee.empty()
                self.game.allboss.empty()
                self.game.alldwarf.empty()
                self.game.allenemiesonaboat.empty()
                self.game.allgobelinarcher.empty()
                self.game.allgobelinarcher.empty()
                self.game.allgobelinmassue.empty()
                self.game.allgoodelf.empty()
                self.game.allgoodelfsword.empty()
                self.game.allwarg.empty()
                self.game.allprojectiles.empty()
                self.game.bossboat.allprojectilesbossboat.empty()
                self.game.warg.allprojectileswargpoison.empty()
                self.game.dwarf.allprojectiledwarf.empty()
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty()
                self.game.boss.allprojectilesboss.empty()
                self.game.bossbalrog.allprojectilesbossbalrog.empty()
                self.game.bossboat.allprojectilesbossboat.empty()
                self.game.bossdwarf.allprojectilesbossdwarf.empty()
                self.game.bosswarg.allprojectilesbosswarg.empty()
                
            if self.game.isplaying: 
                self.game.updatescore(screen)

                for projectile in self.game.player.allprojectiles:
                        if projectile.rect.y <= 0:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allenemies, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allenemiesonaboat, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allwarg, False):
                            projectile.kill()
                        elif projectile_dwarf_hit := pygame.sprite.spritecollide(projectile, self.game.alldwarf, False):
                            projectile.kill()
                        elif projectile_gobelinarcher_hit := pygame.sprite.spritecollide(projectile, self.game.allgobelinarcher, False):
                            projectile.kill()
                        elif projectile_gobelinarcher_hit := pygame.sprite.spritecollide(projectile, self.game.allgobelinmassue, False):
                            projectile.kill()
                        elif projectile_peon_hit := pygame.sprite.spritecollide(projectile, self.game.allpeon, False):
                            projectile.kill()
                        elif projectile_boss_hit := pygame.sprite.spritecollide(projectile, self.game.allboss, False):
                            projectile.kill()
                        elif projectile_bonusattack_hit := pygame.sprite.spritecollide(projectile, self.game.allbonusattack, False):
                            projectile.kill()
                        elif projectile_bonusmelee_hit := pygame.sprite.spritecollide(projectile, self.game.allbonusmelee, False):
                            projectile.kill()
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.enemy.allprojectilesenemy, True):
                            projectile.kill()
                            self.game.score += 1
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.enemyonaboat.allprojectilesenemyonaboat, True):
                            projectile.kill()
                            self.game.score += 1
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.warg.allprojectileswargpoison, True):
                            projectile.kill()
                            self.game.score += 1
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.dwarf.allprojectiledwarf, True):
                            projectile.kill()
                            self.game.score += 1
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.gobelinarcher.allprojectilesgobelinarcher, True):
                            projectile.kill()
                            self.game.score += 1
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.gobelinmassue.allprojectilesgobelinmassue, True):
                            projectile.kill()
                            self.game.score += 1




                for projectile in self.game.goodelf.allprojectilesgoodelf:
                        if projectile.rect.y <= 0:
                            projectile.kill()    
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allenemies, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allenemiesonaboat, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allwarg, False):
                            projectile.kill()
                        elif projectile_dwarf_hit := pygame.sprite.spritecollide(projectile, self.game.alldwarf, False):
                            projectile.kill()
                        elif projectile_gobelinarcher_hit := pygame.sprite.spritecollide(projectile, self.game.allgobelinarcher, False):
                            projectile.kill()
                        elif projectile_gobelinarcher_hit := pygame.sprite.spritecollide(projectile, self.game.allgobelinmassue, False):
                            projectile.kill()
                        elif projectile_peon_hit := pygame.sprite.spritecollide(projectile, self.game.allpeon, False):
                            projectile.kill()

                for projectile in self.game.enemy.allprojectilesenemy:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                       
                for projectile in self.game.enemyonaboat.allprojectilesenemyonaboat:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()

                for projectile in self.game.warg.allprojectileswargpoison:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                
                for projectile in self.game.dwarf.allprojectiledwarf:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()

                for projectile in self.game.gobelinarcher.allprojectilesgobelinarcher:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()

                for projectile in self.game.gobelinmassue.allprojectilesgobelinmassue:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                
                for projectile in self.game.boss.allprojectilesboss:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()

                for projectile in self.game.bossboat.allprojectilesbossboat:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                
                for projectile in self.game.bosswarg.allprojectilesbosswarg:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                
                for projectile in self.game.bossdwarf.allprojectilesbossdwarf:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()

                for projectile in self.game.bossbalrog.allprojectilesbossbalrog:
                        if projectile.rect.y >= 728:
                            projectile.kill() 
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allplayers, False):
                            projectile.kill()
                        elif projectile_enemiesonaboat_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelfsword, False):
                            projectile.kill()
                        elif projectile_warg_hit := pygame.sprite.spritecollide(projectile, self.game.allgoodelf, False):
                            projectile.kill()
                        elif projectile_enemies_hit := pygame.sprite.spritecollide(projectile, self.game.allprojectiles, False):
                            projectile.kill()
                            self.game.allprojectiles.kill()
                       
            else:
                screen.blit(self.banner, (50, 150))
                pygame.display.flip()


            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 0:
                    self.game.startsecondspawn()
                    self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 0:
                show_image(screen, 'dialogue\gandalfstory1.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, 'dialogue\orc story1.png',-10,300)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                self.game.startboss()
                self.game.player.allprojectiles.empty()
                self.game.enemy.allprojectilesenemy.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 0:
                show_image(screen, 'dialogue\orc story2.png',0,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, 'dialogue\gandalfstory2.png',-80,300)
                show_text_window(screen, "Press sur 'C' to continue")
                self.level_number +=1
                level_completed = True       
                self.game.nextlevel()
                show_image_no_scale(screen,r'image\tolacville copie.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image_no_scale(screen,r'image\tolacville copie2.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)             
                self.showing_message = False
                self.game.boss.allprojectilesboss.empty()
                
            if self.level_number == 1:
                self.background = pygame.image.load(r'image\fondlvl1.jpg').convert_alpha()
                level_completed = False
 
            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 1:          
                self.game.startlvl1()
                self.game.allprojectiles.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 1:
                self.game.startlvl1second()
                self.game.allprojectiles.empty()
                self.game.allprojectilesenemyonaboat.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 1:
                show_image(screen, 'dialogue\gandalfstory3.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, 'dialogue\orclacville1.png',0,300)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c) 
                self.game.startbossboat() 
                self.game.enemyonaboat.allprojectilesenemyonaboat.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 1:
                show_image(screen, r'image\boatfond.png',0,0)
                show_image(screen, r'dialogue\gandalfstory4.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, r'dialogue\orclacville2.png',0,300)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c) 
                self.level_number +=1
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_image_no_scale(screen,r'image\wargstory copie.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                self.game.bossboat.allprojectilesbossboat.empty()

            if self.level_number == 2:
                self.background = pygame.image.load(r'image\fondlvl2.png').convert_alpha()
                level_completed = False

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 2:          
                self.game.startlvl2()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 2:
                self.game.startlvl2second()
                self.game.player.allprojectiles.empty()
                self.game.warg.allprojectileswargpoison.empty()
            
            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 2:
                show_image(screen, 'dialogue\wargstory1.png',0,350)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, 'dialogue\gandalfstory5.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                self.game.startbosswarg()
                self.game.warg.allprojectileswargpoison.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 2:
                show_image(screen, r'dialogue\gandalfstory6.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                self.level_number +=1
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_image_no_scale(screen,r'image\tothebluemountain copie.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False

            if self.level_number == 3:
                self.background = pygame.image.load(r'image\fondlvl3.png').convert_alpha()
                level_completed = False

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 3:
                show_image(screen, r'dialogue\gandalfstory7.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)  
                show_image(screen, r'dialogue\nain1story1.png',-5,350)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, r'dialogue\gandalfstory8.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)  
       
                self.game.startlvl3()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 3:
                self.game.startlvl3second()
                self.game.player.allprojectiles.empty()
                self.game.warg.allprojectileswargpoison.empty()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.bossspawned == False and self.level_number == 3:
                show_image(screen, r'dialogue\nain2story1.png',-5,350)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, r'dialogue\gandalfstory9.png',-80,310)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)  
               
                self.game.startbossdwarf()
                self.game.warg.allprojectileswargpoison.empty()
                self.game.player.allprojectiles.empty()

            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 3:
                show_image(screen, r'dialogue\nain2story2.png',-10,350)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, r'dialogue\gandalfstory10.png',-80,310)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)  
                self.level_number +=1
                level_completed = True   
                self.game.nextlevel()
                self.showing_message = True
                show_image_no_scale(screen,r'image\togobelin copie.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                self.game.bossdwarf.allprojectilesbossdwarf.empty()
                self.game.player.allprojectiles.empty()

            if self.level_number == 4:
                self.background = pygame.image.load(r'image\fondlvl4.png').convert_alpha()
                level_completed = False


            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 4:     
                show_image(screen, r'dialogue\gobelinstory1.png',0,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_image(screen, r'dialogue\gandalfstory11.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)       
                self.game.startlvl4()

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.secondspawn == False and self.level_number == 4:
                self.game.startlvl4second()
                self.game.player.allprojectiles.empty()
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty() 


            if self.game.isplaying and self.game.bossspawned == False and self.game.enemyremain == 0 and not level_completed and self.level_number == 4:
                show_image(screen, r'dialogue\gandalfstory12.png',-80,290)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)       
                self.level_number +=1 
                level_completed = True
                self.game.nextlevel()
                self.showing_message = True
                show_text_window(screen, "Level completed! Press sur 'S' to continue")
                wait_for_key_press(pygame.K_s)
                self.showing_message = False
                self.game.firstspawn = False
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty() 

            if self.level_number == 5:
                self.background = pygame.image.load(r'image\fondlvl5.png').convert_alpha()
                level_completed = False  

            if self.game.isplaying and self.game.enemyremain == 0 and self.game.firstspawn == False and self.level_number == 5:          
                self.game.startbossbalrog()
                self.game.gobelinarcher.allprojectilesgobelinarcher.empty()  
                self.game.gobelinmassue.allprojectilesgobelinmassue.empty()  
            
            if self.game.isplaying and self.game.bossspawned == True and self.game.enemyremain == 0 and not level_completed and self.level_number == 5:
                show_image_no_scale(screen,r'image\balrogstory.png',0,0)
                show_text_window(screen, "Press sur 'C' to continue")
                wait_for_key_press(pygame.K_c)
                show_text_window(screen, "Chapter 1 completed, next is coming soon")
                wait_for_key_press(pygame.K_s)
                
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