import pygame

class Sound:

    def __init__(self):
        self.music = pygame.mixer.music.load(r'C:\Users\ponce\Desktop\python\23.10.23.space\son\Lord of the rings ~ Concerning Hobbits 16-bit [2mJPGvsuHUQ].mp3')
        self.music_volume = pygame.mixer.music.set_volume(0.23)
        self.music_play = pygame.mixer.music.play(loops=-1)
        self.explose_sound = pygame.mixer.Sound(r'C:\Users\ponce\Desktop\python\23.10.23.space\son\zombie-death-2-95167.mp3')
        self.explose_boss_sound= pygame.mixer.Sound(r'C:\Users\ponce\Desktop\python\23.10.23.space\son\knife-stab-121084.mp3')
        self.shoot_sound = pygame.mixer.Sound(r'C:\Users\ponce\Desktop\python\23.10.23.space\son\beam-8-43831.mp3')
        self.soundvolume()

    def soundvolume(self):
        self.explose_sound.set_volume(0.15)
        self.shoot_sound.set_volume(0.05)
        self.explose_boss_sound.set_volume(0.15)