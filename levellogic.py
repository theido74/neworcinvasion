import pygame
from maingame import Game

class Level:
    def __init__(self, level_number, background_path):
        self.level_number = level_number
        self.background = pygame.image.load(background_path).convert_alpha()
        self.banner = pygame.image.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\presstoplay.png').convert_alpha()
        self.game = Game()
        self.y_background = 0
        self.running = True

    def run_level(self, screen, clock):
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

            if self.game.isplaying:
                self.game.updatescore(screen)
            else:
                screen.blit(self.banner, (50, 150))
                # Gérer le score ou d'autres éléments spécifiques au niveau

                pygame.display.flip()

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.game.pressed[event.key] = True

                    if event.key == pygame.K_SPACE:
                        self.game.player.launchprojectile()

                    if event.key == pygame.K_s:
                        self.game.start()

                elif event.type == pygame.KEYUP:
                    self.game.pressed[event.key] = False

            if self.game.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x + self.game.player.rect.width < screen.get_width():
                self.game.player.move_right()
            if self.game.pressed.get(pygame.K_LEFT) and self.game.player.rect.x > 0:
                self.game.player.move_left()
            if self.game.pressed.get(pygame.K_DOWN) and self.game.player.rect.y + self.game.player.rect.height < screen.get_height():
                self.game.player.move_up()
            if self.game.pressed.get(pygame.K_UP) and self.game.player.rect.y > 0:
                self.game.player.move_down()
def run_game():
# Initialisation de Pygame
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Space Orc Invasion')
    screen = pygame.display.set_mode((432, 728))

    # Création des niveaux
    level_0 = Level(0, r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\game\fond1.png')
    level_1 = Level(1, r'C:\Users\ponce\Desktop\python\23.10.23.space\Image\fondlvl1.jpg')

    current_level = level_0  # Commencer par le niveau 0

    # Boucle principale du jeu
    running = True
    while running:
        if current_level.level_number == 0:
            current_level.run_level(screen, clock)
            if not current_level.running:  # Si le niveau est terminé
                current_level = level_1  # Passer au niveau suivant
        elif current_level.level_number == 1:
            current_level.run_level(screen, clock)
            if not current_level.running:  # Si le niveau est terminé
                # Par exemple, vous pourriez charger un niveau suivant ici
                pass  # Mettre à jour pour charger d'autres niveaux

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
