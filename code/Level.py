from pygame import Surface, Rect
import pygame
from code.Snake import Snake
from code.Food import Food
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK, SNAKE_VELOCITY, PATH_BG_IMAGEM


class Level:
    def __init__(self, window: Surface):   
        self.window = window
        self.bg_imagem = pygame.image.load(PATH_BG_IMAGEM).convert_alpha() #carega a imagem
        self.background = pygame.transform.scale(self.bg_imagem, (WIN_WIDTH, WIN_HEIGHT))  # Ajusta a imagem ao tamanho da tela
        self.clock = pygame.time.Clock()    
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()

    def level_run(self):
        while True:
            self.events()
            self.to_update()
            self.draw()
            self.clock.tick(SNAKE_VELOCITY) # defini o fps do jogo

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
        self.window.blit(self.background, (0,0))
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()