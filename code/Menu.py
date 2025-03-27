from pygame.font import Font
from pygame import Surface
from pygame import Rect
import pygame
from code.Const import C_ORAGE, WIN_WIDTH, MENU_OPTION, C_YELLOW, C_WHITE, DIFFICULTIES, PATH_BG_IMAGEM_MENU, WIN_HEIGHT




class Menu():
    def __init__(self, window):
        self.window = window
        self.bg_imagem = pygame.image.load(PATH_BG_IMAGEM_MENU).convert_alpha() #carega a imagem
        self.background = pygame.transform.scale(self.bg_imagem, (WIN_WIDTH, WIN_HEIGHT))  # Ajusta a imagem ao tamanho da tela

        

    def run(self):
        self.window.fill((0,0,0))  #reseta a tela
        self.window.blit(self.background, (0,0))


        menu_option = 0
        
        while True:
            self.menu_text(50, "Python Snake", C_ORAGE, ((WIN_WIDTH / 2), 120))
            pygame.display.flip()


            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))


            #checa os eventos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:                        
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        
                        else:
                            menu_option = len(MENU_OPTION)-1 

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
            pygame.display.flip()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    def menu_difficulty(self):
        
        self.window.fill((0,0,0))  #reseta a tela
        self.window.blit(self.background, (0,0))

        menu_option = 0

    
        while True:
            self.menu_text(50, "Selecione a Dificuldade", C_ORAGE, ((WIN_WIDTH / 2), 120))
            pygame.display.flip()


            for i in range(len(DIFFICULTIES)):
                if i == menu_option:
                    self.menu_text(40, DIFFICULTIES[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(40, DIFFICULTIES[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))


            #checa os eventos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        if menu_option < len(DIFFICULTIES) -1:
                            menu_option += 1
                        else:                        
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        
                        else:
                            menu_option = len(DIFFICULTIES)-1 

                    if event.key == pygame.K_RETURN:

                        return DIFFICULTIES[menu_option]
                        
            pygame.display.flip()
