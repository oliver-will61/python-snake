from pygame.font import Font
from pygame import Surface
from pygame import Rect
import pygame
from code.Const import COLOR_ORAGE, WIN_WIDTH


class Menu():
    def __init__(self, window):
        self.window = window

    def run(self):

        while True:
            self.menu_text(50, "Python Snake", COLOR_ORAGE, ((WIN_WIDTH / 2), 120))
            pygame.display.flip()

    



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)