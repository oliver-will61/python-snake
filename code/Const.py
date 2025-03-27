WIN_WIDTH = 1160
WIN_HEIGHT = 660

HUD = {
    'hud_x': 0,
    'hud_y':0,
    'hud_width': WIN_WIDTH,
    'hud_height': 80
} 


BLOCK_SIZE = 20 # tamanho da cobra e da comida

MENU_OPTION = ("JOGAR",
               "Dificuldade",
               "SAIR",)

GAME_OVER_OPTION = ("CONTINUAR",
                    "VOLTAR PARA O MENU")

DIFFICULTIES = ('FÁCIL', 'MÉDIO', 'DÍFICIL')

SNAKE_VELOCITY = {
   DIFFICULTIES[0]: 5, #fácil
   DIFFICULTIES[1]: 10, #médio
   DIFFICULTIES[2]: 20 #dificil
}


#paleta de cores

C_ORAGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (143, 208, 83)
C_BLACK = (26,26,26)
C_YELLOW =  (255, 215, 0)
C_RED =  (255, 0, 60) 
C_RED_ALTERNATIVE = (193, 39, 45)




PATH_BG_IMAGEM = './assets/bg.jpg'
PATH_BG_IMAGEM_MENU = './assets/bg_menu.jpg'

PATH_DATA_JSON = './data.json'

FONT_SIZE_SCORE = 28