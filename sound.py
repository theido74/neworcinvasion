import pygame

class Sound:

    def __init__(self):
        self.music = pygame.mixer.music.load(r'son\Lord of the rings ~ Concerning Hobbits 16-bit [2mJPGvsuHUQ].mp3')
        self.music_volume = pygame.mixer.music.set_volume(0.23)
        self.music_play = pygame.mixer.music.play(loops=-1)
        self.explose_sound = pygame.mixer.Sound(r'son\zombie-death-2-95167.mp3')
        self.explose_boss_sound= pygame.mixer.Sound(r'son\knife-stab-121084.mp3')
        self.boat_sound = pygame.mixer.Sound(r'son\mixkit-jump-in-water-2923.wav')
        self.boatboss_sound = pygame.mixer.Sound(r'son\mixkit-epic-impact-afar-explosion-2782.wav')
        self.warg_sound = pygame.mixer.Sound(r'son\mixkit-wolf-attack-1773.mp3')
        self.wargboss_sound = pygame.mixer.Sound(r'son\whining-dog-6110.mp3')
        self.dwarf_sound = pygame.mixer.Sound(r'son\scary-laugh-123862.mp3')
        self.dwarfboss_sound = pygame.mixer.Sound(r'son\manx27s-cry-122258.mp3')
        self.gobelin_sound = pygame.mixer.Sound(r'son\spade-hacking-sound-with-gore-effects-96909.mp3')
        self.balrog_sound = pygame.mixer.Sound(r'son\forest-monster-scream1-104247.mp3')
        self.peon_sound = pygame.mixer.Sound(r'son\die-47695.mp3')
        self.shoot_sound = pygame.mixer.Sound(r'son\beam-8-43831.mp3')
        self.bonusattack_sound = pygame.mixer.Sound(r'son\fantasy_ui_button_6-102219.mp3')
        self.goodelf_sound = pygame.mixer.Sound(r'son\vmx-molly-good-bye-93235.mp3')

        self.soundvolume()

    def soundvolume(self):
        self.explose_sound.set_volume(0.15)
        self.shoot_sound.set_volume(0.05)
        self.explose_boss_sound.set_volume(0.15)
        self.boat_sound.set_volume(0.15)
        self.warg_sound.set_volume(0.15)
        self.wargboss_sound.set_volume(0.15)
        self.boatboss_sound.set_volume(0.15)
        self.dwarfboss_sound.set_volume(0.15)
        self.dwarf_sound.set_volume(0.15)
        self.gobelin_sound.set_volume(0.15)
        self.balrog_sound.set_volume(0.15)
        self.peon_sound.set_volume(0.05)