import pygame

class Text:
    def __init__(self,screen):
        self.screen = screen          
def show_text_window(screen, text):
    font = pygame.font.Font(r'c:\Users\ponce\AppData\Local\Microsoft\Windows\Fonts\small_pixel.ttf', 14)
    text_surface = font.render(text, True, 'purple', 'gold')
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def wait_for_key_press(key):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == key:
                    waiting = False

textstory1= '''

Gandalf, back from the white shores after a long break, found himself wandering alone in a strangely violet and cybernetic Middle-earth. Tired of the elves' food and their boring music, he decided to embark on a quest to find Aragorn, his old comrade. However, the quest wouldn't be as straightforward as he imagined.

Roaming into a peculiar city, Gandalf stumbled upon a grimy tavern. The place was smoky, flickering lights illuminated strange creatures with greenish skin. These were not elves, oh no, they were cyborg orcs with rusty implants and bolts protruding from their skin.

"Hey, old wizard! You don't seem to like elves as much as we do, huh?" chuckled one of the orcs, spitting on the floor.

Unperturbed, Gandalf replied, "You could say that. Their leafy salads and melodious airs almost made me regret coming back. But I'm not here to discuss my dietary issues. Where's Aragorn?"

The orcs exchanged knowing looks before bursting into laughter. "Ah, Aragorn! We froze him and lost him, old man. He's somewhere between bits and bytes, if you catch my drift."

Gandalf furrowed his brow. "What's this freezing business?"

"You see, he tried to modernize his kingdom with magical freezers, but it went wrong. Now he's somewhere in the cloud, lost like an old forgotten backup," explained an orc, laughing loudly.

Maintaining his composure, Gandalf asked, "Who else knows where he is?"

The orcs glanced at each other, and one leaned in to whisper, "Lady Arwen. She's in exile somewhere, but she holds the keys to the magical fridge."

Gandalf stood up, ready to continue his quest. "Thanks for the information, guys. And by the way, you should consider taking a shower. It stinks in here."

The orcs burst into laughter, seeming to appreciate Gandalf's trashy humor. He left the tavern, heading towards Dame Arwen's mysterious exile, ready to unravel the mystery of Aragorn's freezing in this absurd and cybernetic Middle-earth.
'''