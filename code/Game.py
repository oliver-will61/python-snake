import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK
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
                self.to_update()
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
    
    def to_update (self):
        if self.snake.alive:
            self.snake.to_update_snake()

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.food.new_position()
                self.snake.body.append(self.snake.body[-1])  # Cresce
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]
            if x < 0 or x >= WIN_WIDTH or y < 0 or y >= WIN_HEIGHT:
                self.snake.alive = False
        
        else:
            self.reset()

    def draw(self):
        self.window.fill(C_BLACK)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()

    

            
