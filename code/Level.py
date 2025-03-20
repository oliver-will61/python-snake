from pygame import Surface, Rect
import pygame
from code.Snake import Snake
from code.Food import Food
from code.Const import WIN_WIDTH, WIN_HEIGHT, HUD, C_GREEN, SNAKE_VELOCITY, PATH_BG_IMAGEM, BLOCK_SIZE


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
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]
            print(x, y)

            if x >= WIN_WIDTH:
                print(f'X maior ou igual a 1160 - X:{x}')
                x = 0 # O -20 do block serve para compesar a andada da cobra
                print(f'Valor de X agora é: {x}')
                
            elif x < 0:
                print(f'X menor que 0 - X:{x}')
                x = WIN_WIDTH - BLOCK_SIZE 
                print(f'Valor de X agora é: {x}')

                
            elif y >= WIN_HEIGHT:
                print(f'Y maior ou igual a 660 - Y:{y}')
                y = 0   # O -20 do block serve para compesar a andada da cobra
                print(f'Valor de Y agora é: {y}')
                
            elif y < 0:
                print(f'Y menor que 0 - Y :{y}')
                y = WIN_HEIGHT - BLOCK_SIZE 
                print(f'Valor de Y agora é: {y}')
                

            x = (x // BLOCK_SIZE) * BLOCK_SIZE # '//' faz a divisão inteira garantido que o block_size seja sempre um número multiplo de 20
            y = (y // BLOCK_SIZE) * BLOCK_SIZE # Necessário para a cobra não perder o alinhamento com o grid, caso o contrário ele vai passar por cima da comida
            
            self.snake.body[0] = [x,y]

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.food.new_position()
                self.snake.body.append(self.snake.body[-1])  # Cresce
        
        else:
            self.reset()

    def draw(self):
        self.window.blit(self.background, (0,0))
        self.draw_hud(self.window)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()

    def draw_hud(self, window):
        #desenha retangulo que vai ser usado como hud
        pygame.draw.rect(window, C_GREEN, (HUD['hud_x'],HUD['hud_y'], HUD['hud_width'], HUD['hud_height']))