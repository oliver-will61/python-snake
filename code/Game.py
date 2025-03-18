import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Snake import Snake
from code.Food import Food

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size= (WIN_WIDTH, WIN_HEIGHT))
        self.execution = True
        self.reset()
    
    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            # lida com o retorna da opção que o jogador escolheu na tela de menu
            if menu_return == MENU_OPTION[0]: #inicia o jogo 

                print('jogo inicinado')

                self.events()
                self.update()
                self.draw()

           

            elif menu_return == MENU_OPTION[1]: #mostra o score 
                print('SCORE: Ainda em desenvolvimento')    
            elif menu_return == MENU_OPTION[2]: #sai do jogo 
                quit()

    def reset(self):
        self.snake = Snake()
        self.food = Food()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP') 
                elif event.key  == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key  == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key  == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')


            
