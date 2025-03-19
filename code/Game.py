import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK
from code.Menu import Menu
from code.Level import Level


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size= (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # lida com o retorna da opção que o jogador escolheu na tela de menu
            if menu_return == MENU_OPTION[0]: #inicia o jogo 
                level = Level(self.window)
                level.level_run()

            elif menu_return == MENU_OPTION[1]: #mostra o score 
                print('SCORE: Ainda em desenvolvimento')    
            elif menu_return == MENU_OPTION[2]: #sai do jogo 
                quit()

    

    

            
